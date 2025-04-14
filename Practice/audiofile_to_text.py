import whisper

# 載入 Whisper 模型（用 base 速度快、準度還行）
model = whisper.load_model("base")

# 讀取音檔
audio_path = "example_audio.wav"  # 改成你自己的檔案

print("🎧 分析音檔中...")
result = model.transcribe(audio_path, language="zh")  # 設定中文

print("📝 轉換文字：")
print(result["text"])