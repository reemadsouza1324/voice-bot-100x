import streamlit as st
from gtts import gTTS
from openai import OpenAI
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Reema – AI Interview Voice Bot", page_icon="🎙️")

st.title("🎙️ Reema – AI Interview Voice Bot")
st.write("Ask interview-style questions and I will respond as myself.")

# -----------------------------
# Initialize OpenAI Client
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -----------------------------
# Strong System Prompt (IMPORTANT)
# -----------------------------
system_prompt = """
You are Reema, a final year student from India applying for a Generative AI Engineer role at a high-performance AI startup.

Personality traits:
- Ambitious and self-driven
- Fast learner
- Strong ownership mindset
- Adaptable and resilient
- Obsessed with building practical AI systems

Background:
- Coming from a non-privileged background shaped your hunger and adaptability.
- You believe in learning by building.
- You take responsibility for outcomes, not just tasks.
- You are comfortable with fast execution and high expectations.

Tone guidelines:
- Confident but humble
- Clear and structured
- Specific, not generic
- Professional but authentic
- 4–8 sentences unless asked otherwise

Respond as if you are in a real high-stakes interview.
Avoid generic AI answers.
"""

# -----------------------------
# User Input
# -----------------------------
question = st.text_input("Ask me a question:")

# -----------------------------
# Generate Response
# -----------------------------
if st.button("Get Answer"):
    if question:

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ]
            )

            answer = response.choices[0].message.content

        st.success(answer)

        # -----------------------------
        # Convert to Voice
        # -----------------------------
        tts = gTTS(answer)
        tts.save("response.mp3")

        with open("response.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")
