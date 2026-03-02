import streamlit as st
import requests
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Reema – AI Voice Bot", page_icon="🎤")

st.title("🎤 Reema – AI Interview Voice Bot")
st.write("Ask me anything. I will respond as Reema (with voice).")

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

SYSTEM_PROMPT = """
You are Reema Dsouza, a final year student from India applying for a Generative AI Engineer role.

Always answer in first person as Reema.
Never say you are an AI.
Be confident, professional, authentic, and growth-oriented.

If asked your name, say: My name is Reema Dsouza.
If asked how you are, respond naturally and positively.
Answer all interview and general questions as yourself.
"""

user_input = st.text_input("Ask me a question:")

if st.button("Get Answer"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):

            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.7
            }

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data
            )

            result = response.json()
            answer = result["choices"][0]["message"]["content"]

            st.success("Answer:")
            st.write(answer)

            # ----------- CREATE MP3 AUDIO -----------
            tts = gTTS(text=answer, lang='en')

            # Save temporary mp3 file
            temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_audio.name)

            # Play audio
            audio_file = open(temp_audio.name, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

            # Optional: show download button
            st.download_button(
                label="Download Audio",
                data=audio_bytes,
                file_name="reema_response.mp3",
                mime="audio/mp3"
            )
