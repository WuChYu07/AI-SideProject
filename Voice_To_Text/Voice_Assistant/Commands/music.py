import pygame
import os
import threading
import time
from Voice_Assistant.config import MUSIC_FOLDER

pygame.mixer.init()
current_song = 0

def _get_music_files():
    return [f for f in os.listdir(MUSIC_FOLDER) if f.endswith('.mp3')]

def play():
    songs = _get_music_files()
    if not songs:
        print("No Music Files!")
        return

    global current_song
    for i in range(current_song, len(songs)):
        current_song = i
        path = os.path.join(MUSIC_FOLDER, songs[i])
        print(f"Playing: {songs[i]}")
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        # Wait for music to finish
        while pygame.mixer.music.get_busy():
            time.sleep(1)

def next_song():
    songs = _get_music_files()
    global current_song
    if songs:
        current_song = (current_song + 1) % len(songs)
        play_music_backround()

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped!!")

def play_music_backround():
    thread = threading.Thread(target=play)
    thread.start()

if __name__ == "__main__":
    play()
