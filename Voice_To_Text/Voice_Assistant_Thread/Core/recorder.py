import sounddevice as sd
import wavio
import tempfile

def record_audio(duration=4, samplerate= 44100):
    print("Please talking...")
    audio = sd.rec(int(samplerate*duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    tmp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name

    wavio.write(tmp_path, audio, samplerate, sampwidth=2)

    return tmp_path

