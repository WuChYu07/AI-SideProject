import pygame
import os
import threading
import time
from Voice_Assistant.config import MUSIC_FOLDER

pygame.mixer.init()
current_song = 0
playback_thread = None
stop_flag = threading.Event()

def _get_music_files():
    return [f for f in os.listdir(MUSIC_FOLDER) if f.endswith('.mp3')]

def _play_music_loop(songs, play_once_mode, loop_mode):
    global current_song
    while not stop_flag.is_set():
        if current_song >= len(songs):
            if play_once_mode.is_set():
                break
            current_song = 0  # Loop mode restart

        path = os.path.join(MUSIC_FOLDER, songs[current_song])
        print(f"🎵 Playing: {songs[current_song]}")
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            if stop_flag.is_set():
                return
            time.sleep(0.5)

        current_song += 1
        if play_once_mode.is_set() and current_song >= len(songs):
            break

def start_playback_thread(songs, play_once_mode, loop_mode):
    global playback_thread
    playback_thread = threading.Thread(
        target=_play_music_loop, args=(songs, play_once_mode, loop_mode)
    )
    playback_thread.start()

def play(play_once_mode, loop_mode):
    global stop_flag, playback_thread
    songs = _get_music_files()
    if not songs:
        print("No Music Files!")
        return

    if playback_thread and playback_thread.is_alive():
        print("🎶 Already playing...")
        return

    stop_flag.clear()
    start_playback_thread(songs, play_once_mode, loop_mode)

def next_song(play_once_mode, loop_mode):
    global current_song, stop_flag
    songs = _get_music_files()
    if not songs:
        return

    stop_flag.set()
    pygame.mixer.music.stop()

    current_song = (current_song + 1) % len(songs)
    stop_flag.clear()
    start_playback_thread(songs, play_once_mode, loop_mode)
    print(f"⏭️ Next: {songs[current_song]}")

def stop_music():
    global stop_flag
    stop_flag.set()
    pygame.mixer.music.stop()
    print("⏹️ Music stopped!")
