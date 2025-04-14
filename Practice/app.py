import streamlit as st #快速建立互動式網頁應用
import whisper
import tempfile #建立臨時檔案或臨時資料夾

st.title("🎤 語音轉文字 Demo App") #顯示 App 的標題，大字體
st.write("上傳一個音訊檔（支援 .wav / .mp3），系統會自動轉成文字。") #顯示說明文字

#檔案上傳按鈕。type 限制可接受的副檔名。
uploaded_file = st.file_uploader("請上傳音訊檔", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    # 將檔案儲存為暫存檔（Whisper 要吃檔案路徑）
    # 建立一個具名的臨時檔案（也就是有路徑可以存取的），副檔名是 .mp3。
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read()) #把上傳的音訊內容寫進這個臨時檔案裡。
        tmp_path = tmp_file.name #存下臨時檔案的路徑，稍後要交給 Whisper 使用。

    st.audio(uploaded_file, format="audio/mp3")

    st.write("🧠 開始辨識語音...請稍候")

    model = whisper.load_model("base")
    result = model.transcribe(tmp_path, language="zh")

    st.success("辨識完成！")
    st.markdown("### 📝 辨識結果：")
    st.write(result["text"])