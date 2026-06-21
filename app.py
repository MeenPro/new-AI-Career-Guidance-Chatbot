
import streamlit as st
import requests

# OpenRouter API Key
API_KEY = st.secrets["OPENROUTER_API_KEY"]

# Page Title
st.set_page_config(page_title="AI Career Guidance Chatbot")
st.title("AI Career Guidance Chatbot")

# Student Details
name = st.text_input("Enter Your Name")

branch = st.selectbox(
    "Select Your Branch",
    ["ECE", "CSE", "EEE", "Mechanical"]
)

interest = st.selectbox(
    "Select Your Interest",
    ["AI", "VLSI", "Embedded Systems", "Cyber Security"]
)

skills = st.text_input(
    "Enter Your Skills (Example: Python, Arduino)"
)

user_question = st.text_area(
    "Ask an AI Career Question"
)

# Button
if st.button("Get Career Recommendation"):

    # Student Profile
    st.write("## Student Profile")
    st.write("**Name:**", name)
    st.write("**Branch:**", branch)
    st.write("**Interest:**", interest)
    st.write("**Skills:**", skills)

    # AI Career Guidance
    if user_question:

        prompt = f"""
Student Name: {name}
Branch: {branch}
Interest: {interest}
Skills: {skills}

Question:
{user_question}

Give:
1. Personalized Career Guidance
2. Career Roadmap
3. Required Skills
4. Certifications
5. Job Opportunities
6. Salary Expectations
"""

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "meta-llama/llama-3.3-8b-instruct:free",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                }
            )

            result = response.json()

            st.write("## Debug Response")
            st.json(result)

            if "choices" in result:
                ai_response = result["choices"][0]["message"]["content"]

                st.write("## AI Career Guidance")
                st.write(ai_response)

            elif "error" in result:
                st.error(f"OpenRouter Error: {result['error']}")

            else:
                st.error(f"Unexpected Response: {result}")

        except Exception as e:
            st.error(f"AI Error: {e}")

    # Skill Gap Analysis
    st.write("## Skill Gap Analysis")

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
            "Microcontrollers",
            "Arduino"
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

    # Career Recommendations
    st.write("## Career Recommendations")

    if interest == "AI":

        st.success("Recommended Career: Machine Learning Engineer")

        st.write("### Courses")
        st.write("- Python for Data Science")
        st.write("- Machine Learning")
        st.write("- Deep Learning")
        st.write("- TensorFlow")

    elif interest == "VLSI":

        st.success("Recommended Career: VLSI Design Engineer")

        st.write("### Courses")
        st.write("- Digital Electronics")
        st.write("- Verilog HDL")
        st.write("- FPGA Design")
        st.write("- ASIC Design")

    elif interest == "Cyber Security":

        st.success("Recommended Career: Cyber Security Analyst")

        st.write("### Courses")
        st.write("- Networking Fundamentals")
        st.write("- Linux Essentials")
        st.write("- Ethical Hacking")
        st.write("- Web Security")

        st.write("### Certifications")
        st.write("- Google Cybersecurity")
        st.write("- CompTIA Security+")
        st.write("- CEH")

    else:

        st.success("Recommended Career: Embedded Systems Engineer")

        st.write("### Courses")
        st.write("- C Programming")
        st.write("- Arduino Programming")
        st.write("- Embedded C")
        st.write("- ARM Microcontrollers")

