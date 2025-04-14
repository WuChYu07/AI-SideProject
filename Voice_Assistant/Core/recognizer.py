import whisper
import time
from Voice_Assistant.Core.recorder import record_audio
from Voice_Assistant.Core.command_router import handle_command

model = whisper.load_model("base")

language = "en" #zh is mandatory, en is English
def detect_keywords():
    print("🎧 Stand by...(Please say player to further actions")
    while True:
        audio_path = record_audio(duration=2)
        result = model.transcribe(audio_path, language=language)
        text = result["text"]
        print(f" Stand by...：{text}")
        text = text.strip()

        if text.startswith("music") or text.startswith("Music") :
            print("🎤 Commands mode, Speak command...")
            command_loop()


def command_loop():
    audio_path = record_audio(duration=3)
    result = model.transcribe(audio_path, language=language)
    text = result["text"]
    print(f"identifying：{text}")
    handle_command(text)

