# main.py

import threading
import queue
import time
from Voice_Assistant_Thread.Commands.music import play, stop_music, next_song
from Voice_Assistant_Thread.Core.recorder import record_audio
import whisper

# Init Whisper
model = whisper.load_model("base")
language = "en"

# Thread-safe Queue for commands
command_queue = queue.Queue()
is_playing = threading.Event()  # If music is plaoying
loop_mode = threading.Event()       # if loop_mode
play_once_mode = threading.Event()  # if play whole file one time

# 🎧 Voice Recognition Thread
def recognizer_thread():
    print("🎧 Stand by...(say 'music' to start player)")
    while True:
        audio_path = record_audio(duration=2)
        result = model.transcribe(audio_path, language=language)
        text = result["text"].strip().lower()
        print(f"🎧 Heard: {text}")

        if "music" in text:
            print("🎤 Entering music command mode...")
            command_loop()


def command_loop():
    while True:
        audio_path = record_audio(duration=3)
        result = model.transcribe(audio_path, language=language)
        text = result["text"].strip().lower()
        print(f"🎤 Command: {text}")

        if text in ["exit", "stop listening"]:
            print("🔁 Returning to standby...")
            break
        elif text.startswith("play"):
            command_queue.put("play")
        elif text.startswith("stop") :
            command_queue.put("stop")
        elif text.startswith("next"):
            command_queue.put("next")
        elif text.startswith("end"):
            play_once_mode.set()
            loop_mode.clear()
        elif text.startswith("loop"):
            loop_mode.set()
            play_once_mode.clear()
        else:
            print("❓ Unknown command")


# 🔊 Music Controller Thread
def music_player_thread():
    while True:
        command = command_queue.get()
        if command == "play":
            if not is_playing.is_set():
                is_playing.set()
                print("✅Starting music...")
                play(play_once_mode, loop_mode)
                is_playing.clear()
        elif command == "stop":
            stop_music()
            play_once_mode.clear()
            loop_mode.clear()
            is_playing.clear()
        elif command == "next":
            stop_music()
            next_song(play_once_mode, loop_mode)
        command_queue.task_done()


# 🔁 Thread setup
if __name__ == "__main__":
    # Start music controller thread
    threading.Thread(target=music_player_thread, daemon=True).start()

    # Start recognizer
    recognizer_thread()
