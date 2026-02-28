import streamlit as st

st.set_page_config(page_title="Reema AI Voice Bot")

st.title("🎙️ Reema – AI Interview Bot")

st.write("Ask interview questions and I will answer as myself.")

answers = {
    "life story": "I am a final year student from India who is actively learning and experimenting with AI tools. Coming from a non privileged background taught me adaptability and resilience. I enjoy building practical solutions and learning by doing.",
    "superpower": "My biggest strength is my ability to learn fast and adapt quickly. Even if I do not know something, I figure it out using research, AI tools, and experimentation.",
    "grow": "The top three areas I want to grow in are public speaking, deeper understanding of AI systems, and leadership skills.",
    "misconception": "Some people think I am quiet or reserved, but once comfortable I contribute actively and take ownership of my work.",
    "boundaries": "I push my limits by taking on uncomfortable challenges, building real projects, and continuously improving through feedback."
}

question = st.text_input("Type your interview question:")

if st.button("Get Answer"):
    response = "That is a great question. I am always learning and growing."
    for key in answers:
        if key in question.lower():
            response = answers[key]
    st.success(response)
