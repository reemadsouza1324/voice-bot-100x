import streamlit as st

st.set_page_config(page_title="Reema AI Voice Bot")

st.title("🎙️ Reema – AI Interview Voice Bot")

st.write("Ask interview questions and I will answer as myself.")

answers = {
    "life story": "I am a student from India who is actively learning and experimenting with AI tools. I come from a non privileged background which taught me adaptability and self learning. I enjoy building practical solutions and continuously improving myself.",
    
    "superpower": "My biggest strength is my ability to learn fast and adapt. Even if I do not know something initially, I quickly figure it out using research, AI tools, and experimentation.",
    
    "grow": "The top three areas I want to grow in are public speaking, deeper understanding of AI systems, and leadership skills in collaborative team environments.",
    
    "misconception": "Some people think I am quiet or reserved, but once I am comfortable, I actively contribute ideas and take ownership of responsibilities.",
    
    "boundaries": "I push my limits by intentionally taking on tasks that feel uncomfortable, building real projects instead of just learning theory, and using feedback as a tool for improvement."
}

question = st.text_input("Type your interview question:")

if st.button("Get Answer"):
    response = "That is a great question. I am always learning and growing."

    for key in answers:
        if key in question.lower():
            response = answers[key]

    st.success(response)

    # Browser-based voice output
    st.markdown(f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{response}");
        window.speechSynthesis.speak(msg);
        </script>
    """, unsafe_allow_html=True)
