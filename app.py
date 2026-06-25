import streamlit as st
import requests

st.set_page_config(page_title="AI Career Guidance Chatbot", page_icon="🤖")

import os

API_KEY = os.getenv("OPENROUTER_API_KEY")

st.title("🤖 AI Career Guidance Chatbot")

# Sidebar Profile
with st.sidebar:
    st.header("Student Profile")

    name = st.text_input("Name", "Prince")

    branch = st.selectbox(
        "Branch",
        ["ECE", "CSE", "EEE", "Mechanical"]
    )

    interest = st.selectbox(
        "Interest",
        ["AI", "VLSI", "Embedded Systems", "Cyber Security"]
    )

    skills = st.text_input(
        "Skills",
        "Arduino"
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask your career question...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    profile_context = f"""
    Student Name: {name}
    Branch: {branch}
    Interest: {interest}
    Skills: {skills}

    You are an AI Career Guidance Assistant.

    Give:
    - Career Guidance
    - Roadmap
    - Skill Gap Analysis
    - Certifications
    - Job Roles
    - Salary Expectations

    Answer naturally like ChatGPT.
    """

    messages = [
        {
            "role": "system",
            "content": profile_context
        }
    ]

    messages.extend(st.session_state.messages)

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "google/gemma-3-4b-it",
                "messages": messages,
                "temperature": 0.7
            }
        )

        result = response.json()

        if "choices" in result:

            ai_response = result["choices"][0]["message"]["content"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": ai_response
                }
            )

            with st.chat_message("assistant"):
                st.markdown(ai_response)

        elif "error" in result:
            st.error(result["error"]["message"])

        else:
            st.error("Unexpected API response")

    except Exception as e:
        st.error(f"Error: {e}")

# Skill Gap Analysis
st.divider()
st.subheader("📊 Skill Gap Analysis")

if interest == "AI":
    required_skills = [
        "Python",
        "Machine Learning",
        "Deep Learning"
    ]

elif interest == "VLSI":
    required_skills = [
        "Verilog",
        "VHDL",
        "SystemVerilog"
    ]

elif interest == "Cyber Security":
    required_skills = [
        "Networking",
        "Linux",
        "Python"
    ]

else:
    required_skills = [
        "C Programming",
        "Arduino",
        "Microcontrollers"
    ]

student_skills = [
    s.strip()
    for s in skills.split(",")
    if s.strip()
]

missing_skills = [
    skill
    for skill in required_skills
    if skill not in student_skills
]

st.write("### Your Skills")
st.write(student_skills)

st.write("### Missing Skills")
st.write(missing_skills)
