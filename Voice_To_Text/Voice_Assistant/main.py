from Core.recorder import record_audio
from Voice_Assistant.Core.recognizer import detect_keywords
from Voice_Assistant.Core.command_router import handle_command

def main():
    detect_keywords()

if __name__ == "__main__":
    main()