from Voice_Assistant.Commands import music

def handle_command(text):
    text = text.strip()
    if text.startswith("music") or text.startswith("Music"):
        music.play_music_backround()

    elif text.lower().startswith("switch") or text.startswith("Switch"):
        music.next_song()

    elif text.startswith("stop") or text.startswith("Stop"):
        music.stop_music()

    else:
        print("⚠️ Cannot identifying commands")
