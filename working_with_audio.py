import streamlit as st
from gtts import gTTS
import io


text = "Hello, welcome to this testing code"
speech = gTTS(text=text, lang='en', slow=False)

audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)

st.audio(audio_buffer)