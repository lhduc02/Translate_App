import streamlit as st
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io


# Khai báo
text, src1, dest1 = "", "", ""


# Chuyển ngôn ngữ　text2text
def trans(text, source, destination):
    translator = Translator()
    translation = translator.translate(text, src=source, dest=destination)
    doc2 = translation.text
    return doc2


# Chuyển ngôn ngữ　text2speech
def text2speech(txt, language):
    tts = gTTS(txt, lang=language)
    # Chuyển đổi giọng nói thành đối tượng AudioSegment
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    audio = AudioSegment.from_mp3(audio_data)
    # Phát âm thanh
    play(audio)


# Tạo interface
st.title("***** Translate Application *****")
st.write()

select1, select2 = st.columns(2)
pa1, pa2, pa3, pa4, pa5 = st.columns(5)
lst_lang1 = ["Tiếng Việt ", "Tiếng Anh", "Tiếng Nhật", "Tiếng Trung", "Tiếng Tây Ban Nha", "Tiếng Pháp"]
lst_lang2 = ["Tiếng Việt", "Tiếng Anh", "Tiếng Nhật", "Tiếng Trung", "Tiếng Tây Ban Nha", "Tiếng Pháp"]
with select1:
    lang1 = st.selectbox("Chọn ngôn ngữ: ", lst_lang1)
    st.write()
    doc1 = st.text_area("Nhập văn bản cần dịch:")
with select2:
    lang2 = st.selectbox("Chọn ngôn ngữ: ", lst_lang2)
    st.write()
    st.write("Bản dịch:")

lst_lang_kyhieu = ['vi', 'en', 'ja', 'zh-cn', 'es', 'fr']
src = lst_lang_kyhieu[lst_lang1.index(lang1)]
dest = lst_lang_kyhieu[lst_lang2.index(lang2)]

with pa3:
    doc_doc1 = st.button("Đọc") # Đọc văn bản cần dịch

with pa5:
    doc_doc2 = st.button("Đọc ") # Đọc văn bản đã dịch


# Main
if len(doc1) != 0 and len(src) != 0 and len(dest) != 0:
    with select2:
        doc2 = trans(doc1, src, dest)
        st.write(doc2)

if doc_doc1:
    text2speech(doc1, src)

if doc_doc2:
    text2speech(doc2, dest)


