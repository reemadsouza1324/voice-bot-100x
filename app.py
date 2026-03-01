import streamlit as st
from openai import OpenAI
from gtts import gTTS
import tempfile

# Page settings
st.set_page_config(page_title="Reema – AI Interview Voice Bot", page_icon="🎤")

st.title("🎤 Reema – AI Interview Voice Bot")
st.write("Ask interview-style questions and I will respond with text and voice.")

# OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# User input
user_input = st.text_input("Ask me a question:")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):

            try:
                # 🔹 Get AI response
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are Reema, answering interview questions professionally and confidently."
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ],
                    temperature=0.7
                )

                answer = response.choices[0].message.content

                st.success("Answer:")
                st.write(answer)

                # 🔹 Convert text to speech
                tts = gTTS(answer)
                
                # Save audio to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.save(fp.name)
                    st.audio(fp.name)

            except Exception as e:
                st.error("Error: Check your API key and billing.")
