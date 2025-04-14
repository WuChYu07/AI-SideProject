import streamlit as st
from audiorecorder import audiorecorder
import whisper
import tempfile
import datetime

# title
st.set_page_config(page_title="語音轉文字 App", layout="centered")
st.title("🎤 即時語音轉文字 App")
st.markdown("上傳音訊檔或直接錄音，我們會幫你轉成文字！")

#-----Choose Language-----------
lang_option = st.selectbox("選擇語言", options=["中文", "英文"])
lang_code = "zh" if lang_option == "中文" else "en"

#-----Load Model------
model = whisper.load_model("base")

#----Upload Files------------
uploaded_file = st.file_uploader("或上傳音訊檔（wav/mp3/m4a）", type=["wav", "mp3", "m4a"])

#-------Fuctionality of Record-------------
st.markdown("點擊開始錄音")
audio = audiorecorder("🔴 點我開始 / 停止錄音", "🎙️ 錄音中...")

#-----------Start to Recognize-------------
if uploaded_file or len(audio) > 0:
    with st.spinner("🧠 辨識中，請稍候..."):
        if uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name
        else:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                audio.export(tmp_file, format="wav") #numpy 音訊陣列 轉為二進位格式
                tmp_path = tmp_file.name

        # Play audio
        st.audio(tmp_path)

        #Recognize
        result = model.transcribe(tmp_path, language=lang_code)

        #Demo
        st.success("辨識完成 ✅")
        st.markdown("### 📝 辨識結果：")
        st.write(result["text"])

        #DownLoad Button
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"transcript_{timestamp}.txt"
        st.download_button("📄 下載文字結果", result["text"], file_name=file_name)