import streamlit as st
from gtts import gTTS
import openai
import os

st.title("🎙️ Reema's Voice Bot")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_input("Ask me anything:")

if st.button("Get Answer"):
    if user_input != "":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        answer = response.choices[0].message["content"]

        st.write(answer)

        # Convert text to speech
        tts = gTTS(answer)
        tts.save("response.mp3")

        # Play audio in browser
        audio_file = open("response.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")
