if st.button("Get Answer"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
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

        # 🔒 SAFE CHECK
        if "choices" not in result:
            st.error("API Error:")
            st.write(result)
        else:
            answer = result["choices"][0]["message"]["content"]

            st.subheader("💬 Text Response:")
            st.write(answer)

            from gtts import gTTS
            import tempfile

            tts = gTTS(text=answer, lang="en")
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)

            audio_file = open(temp_file.name, "rb")
            audio_bytes = audio_file.read()

            st.subheader("🔊 Voice Response:")
            st.audio(audio_bytes, format="audio/mp3")
