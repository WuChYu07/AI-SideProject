import speech_recognition as sr

# 建立辨識器
recognizer = sr.Recognizer()

# 使用麥克風錄音
with sr.Microphone() as source:
    print("🎤 請開始說話...")
    recognizer.adjust_for_ambient_noise(source)  # 自動降噪
    audio = recognizer.listen(source, timeout=5)

print("🧠 正在辨識語音...")

# 語音轉文字
try:
    text = recognizer.recognize_google(audio, language='zh-TW')  # 支援中文
    print("📝 辨識結果：", text)
except sr.UnknownValueError:
    print("😅 無法辨識語音")
except sr.RequestError as e:
    print("❌ API 請求錯誤：", e)