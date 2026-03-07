import streamlit as st
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Reema AI Interview Voice Bot", page_icon="🎤")

st.title("🎤 Reema – AI Interview Voice Bot")
st.write("Ask me anything. I will respond as Reema (text + voice).")

# ------------------ ANSWER FUNCTION ------------------

def generate_answer(question):
    question = question.lower()

    if "name" in question:
        return "My name is Reema Dsouza. I am from Mangalore, Karnataka."

    elif "how are you" in question:
        return "I am doing well and feeling excited about growing in the field of AI and analytics."
        
    elif "Hey / hi /Hii" in question:
        return "Hello !"
        
    elif "life story" in question:
        return "I come from Mangalore, Karnataka, and my journey has been shaped by discipline, resilience, and curiosity. Growing up, I learned the importance of hard work and adaptability. Pursuing Computer Science and Statistics has strengthened my analytical thinking, and I continuously push myself to learn skills that prepare me for real-world challenges."

    elif "superpower" in question:
        return "My number one superpower is my ability to learn quickly and adapt to new situations. Even if I do not know something at first, I take initiative to research, practice, and master it efficiently."

    elif "top 3" in question and "grow" in question:
        return "The top three areas I would like to grow in are advanced AI and Machine Learning concepts, professional communication and public speaking, and leadership skills in technical and team-based environments."

    elif "misconception" in question:
        return "Some coworkers initially think I am quiet or reserved. However, once I understand the environment and goals, I actively contribute ideas, take responsibility, and collaborate confidently with the team."

    elif "push your boundaries" in question or "limits" in question:
        return "I push my boundaries by taking on challenging tasks that stretch my current skill level. Instead of avoiding difficult problems, I approach them as learning opportunities and stay consistent until I improve."

    elif "introduce yourself" in question or "about yourself" in question:
        return "I am currently pursuing BSc in Computer Science and Statistics at St Aloysius College, Mangalore, graduating in July 2026. I have a strong foundation in statistics and programming, and I enjoy applying analytical thinking to real world problems. I completed a data analytics internship and worked on rainfall trend analysis. I am adaptable, curious, and always ready to learn."

    elif "career objective" in question:
        return "I am looking for an entry level role where I can apply my analytical thinking and technical skills while continuously learning. I am open to analysis, development, or operations roles where I can contribute meaningfully to a team."

    elif "education" in question:
        return "I am pursuing BSc in Computer Science and Statistics at St Aloysius College Autonomous, Mangalore, and I will graduate in July 2026."

    elif "internship" in question:
        return "I worked as a Data Analytics Intern at Zephyr Technologies Private Limited. I worked on a rainfall analysis project where I analysed historical weather data, cleaned datasets, and identified seasonal rainfall trends."

    elif "project" in question:
        return "My rainfall analysis project involved analysing historical weather datasets, performing data cleaning and normalization, and identifying seasonal rainfall trends using analytical techniques."

    elif "research" in question:
        return "I authored a research paper on the convergence of pure and applied mathematics, focusing on how AI and statistical modelling can solve real world problems."

    elif "strength" in question:
        return "My biggest strength is my quick adaptability and ability to learn new concepts fast. I also have strong attention to detail and teamwork skills."

    elif "weakness" in question:
        return "I sometimes focus too much on small details, but I am learning to balance perfection with efficiency."

    elif "technical skill" in question or "skills" in question:
        return "My technical skills include Python, SQL, Excel, Google Sheets, Power BI basics, and Microsoft tools like Word and PowerPoint. I also have strong fundamentals in statistics and data analysis."

    elif "soft skill" in question:
        return "My soft skills include communication, teamwork, time management, attention to detail, and quick adaptability."

    elif "why should we hire you" in question:
        return "You should hire me because I bring analytical thinking, adaptability, and a genuine willingness to learn. I am disciplined, curious, and ready to contribute effectively."

    elif "achievement" in question:
        return "Some of my achievements include participating in the national level Datamaze fest at Christ University, being selected for a national level Konkani singing competition in 2023, authoring a research paper, and leading science fests like Xavicon and Imprints 2025."

    elif "leadership" in question:
        return "I have served as a volunteer and core committee member for multiple college events and also led science fests, which helped me develop leadership and organizational skills."

    elif "hobby" in question:
        return "My hobbies include playing volleyball, throwball, shuttle badminton, cycling, singing, travelling, exploring new cultures, and theatre activities."

    elif "five years" in question:
        return "In five years, I see myself as a skilled data or AI professional contributing to impactful projects while continuously upgrading my technical skills."

    elif "salary" in question:
        return "As a fresher, I am open to a fair and competitive package based on my skills and the role responsibilities."

    elif "team" in question:
        return "I enjoy working in teams because collaboration allows us to combine strengths and achieve better results."

    elif "pressure" in question:
        return "I handle pressure by organizing tasks clearly and focusing on one step at a time."

    elif "where are you from" in question or "location" in question:
        return "I am from Mangalore, Karnataka."

    else:
        return "That is an interesting question. I believe my foundation in statistics and computer science, combined with my adaptability and eagerness to learn, helps me approach new challenges confidently."

# ------------------ USER INPUT ------------------

user_input = st.text_input("Ask me a question:")

if st.button("Get Answer"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = generate_answer(user_input)

        # TEXT OUTPUT
        st.subheader("💬 Text Response:")
        st.write(answer)

        # AUDIO OUTPUT
        tts = gTTS(text=answer, lang="en")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        audio_file = open(temp_file.name, "rb")
        audio_bytes = audio_file.read()

        st.subheader("🔊 Voice Response:")
        st.audio(audio_bytes, format="audio/mp3")
