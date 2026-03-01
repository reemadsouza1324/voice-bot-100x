import streamlit as st
from gtts import gTTS
from openai import OpenAI
import os

st.set_page_config(page_title="Reema AI Voice Bot")

st.title("🎙️ Reema – AI Interview Voice Bot")
st.write("Ask interview questions and I will respond as myself.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("Ask me a question:")

if st.button("Get Answer"):
    if question:

        system_prompt = """
        You are Reema, a final year student from India applying for an AI role.
        Answer interview questions in a confident, thoughtful, and authentic way.
        Keep answers clear, concise, and professional.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content

        st.success(answer)

        tts = gTTS(answer)
        tts.save("response.mp3")

        audio_file = open("response.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")
