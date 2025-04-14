FOR Voice_Assistant_Thread

🧠 AI Voice Assistant – Music Controller 🎵
This is a Python-based AI voice assistant capable of controlling music playback through speech commands using OpenAI's Whisper speech recognition model. It supports play, stop, next, and loop functionalities — all through your voice. 🎙️

🚀 Features
🎧 Voice-controlled commands using Whisper AI
🔁 Support for looping or single playback mode
⏯️ Music playback powered by pygame
🧵 Multi-threaded: Voice recognition and music control run independently
🧠 Simple, modular design – easy to understand and extend
🗣️ Voice Commands
- Command	Action
- music	Enters music control mode
- play	Starts music playback
- next	Skips to the next song
- stop	Stops the music
- loop	Enables loop mode
- end	Plays each song once only
- exit / stop listening	Exits command mode
- 
🛠️ Tech Stack
Python 3.10+
Whisper by OpenAI
pygame for music playback
threading for concurrent tasks
queue for command handling

📁 Project Structure
Voice_Assistant_Thread/
│
├── Core/
│   └── recorder.py       # Handles voice recording
│
├── Commands/
│   └── music.py          # Music control logic
│
├── config.py             # Path configuration
├── main.py               # Entry point
└── README.md             # You're reading it!

▶️ Getting Started
Install dependencies
pip install -r requirements.txt
Prepare your music folder
Put .mp3 files inside the MUSIC_FOLDER path defined in config.py.
Run the app
python main.py

📌 Requirements
Python 3.10+
ffmpeg (Whisper needs it to process audio)

🎯 Demo Use Case
Imagine you’re cooking or working and want to control your music hands-free. Just say:
music
play
next
loop
stop
And let your voice assistant handle the rest. No clicks needed. 🔥

🧠 Future Improvements (Ideas)
Add pause/resume support
Integrate with Spotify API
Add voice feedback (TTS)
Build GUI for easier control

💬 Connect
If you like this project, give it a ⭐ or reach out. I'd love to hear feedback or collaborate on AI ideas!
