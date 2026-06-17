import streamlit as st
import google.generativeai as genai

# Gemini API Configuration
genai.configure(api_key="AQ.Ab8RN6Ll75BVcdtIphyQqtqEiP5cdDTyRmsaaqVR-vklJNwE7A")

model = genai.GenerativeModel("gemini-2.5-flash")

# Title
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
    st.write("Name:", name)
    st.write("Branch:", branch)
    st.write("Interest:", interest)
    st.write("Skills:", skills)

    # AI Career Guidance
    if user_question:

        prompt = f"""
        Student Name: {name}
        Branch: {branch}
        Interest: {interest}
        Skills: {skills}

        Question:
        {user_question}

        Give personalized career guidance,
        roadmap, certifications, required skills,
        and future opportunities.
        """

        try:
            response = model.generate_content(prompt)

            st.write("## AI Career Guidance")
            st.write(response.text)

        except Exception as e:
            st.error(f"Gemini Error: {e}")

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

    st.write("Your Skills:", student_skills)
    st.write("Missing Skills:", missing_skills)

    # Career Recommendation

    if interest == "AI":

        st.success("Career: Machine Learning Engineer")

        st.write("### Skills Required")
        st.write("- Python")
        st.write("- Machine Learning")
        st.write("- Deep Learning")

        st.write("### Learning Roadmap")
        st.write("1. Learn Python")
        st.write("2. Learn Machine Learning")
        st.write("3. Learn Deep Learning")
        st.write("4. Build AI Projects")
        st.write("5. Apply for Internships")

        st.write("### Recommended Courses")
        st.write("- Python for Data Science")
        st.write("- Machine Learning")
        st.write("- Deep Learning")
        st.write("- TensorFlow")

    elif interest == "VLSI":

        st.success("Career: VLSI Design Engineer")

        st.write("### Skills Required")
        st.write("- Verilog")
        st.write("- VHDL")
        st.write("- SystemVerilog")

        st.write("### Learning Roadmap")
        st.write("1. Learn Digital Electronics")
        st.write("2. Learn Verilog HDL")
        st.write("3. Practice FPGA Projects")
        st.write("4. Learn ASIC Design Flow")
        st.write("5. Apply for VLSI Internships")

        st.write("### Recommended Courses")
        st.write("- Digital Electronics")
        st.write("- Verilog HDL")
        st.write("- FPGA Design")
        st.write("- ASIC Design Flow")

    elif interest == "Cyber Security":

        st.success("Career: Cyber Security Analyst")

        st.write("### Skills Required")
        st.write("- Networking")
        st.write("- Linux")
        st.write("- Ethical Hacking")
        st.write("- Python")
        st.write("- Web Security")

        st.write("### Learning Roadmap")
        st.write("1. Learn Computer Networking")
        st.write("2. Learn Linux Fundamentals")
        st.write("3. Learn Python Programming")
        st.write("4. Learn Ethical Hacking")
        st.write("5. Practice on TryHackMe")
        st.write("6. Learn Web Security")

        st.write("### Recommended Courses")
        st.write("- Networking Fundamentals")
        st.write("- Linux Essentials")
        st.write("- Ethical Hacking")
        st.write("- Web Application Security")

        st.write("### Recommended Certifications")
        st.write("- Google Cybersecurity Certificate")
        st.write("- CompTIA Security+")
        st.write("- CEH")
        st.write("- Cisco CyberOps Associate")

    else:

        st.success("Career: Embedded Systems Engineer")

        st.write("### Skills Required")
        st.write("- C Programming")
        st.write("- Microcontrollers")
        st.write("- Arduino")

        st.write("### Learning Roadmap")
        st.write("1. Learn C Programming")
        st.write("2. Learn Arduino")
        st.write("3. Learn Microcontrollers")
        st.write("4. Build Embedded Projects")
        st.write("5. Apply for Internships")

        st.write("### Recommended Courses")
        st.write("- C Programming")
        st.write("- Arduino Programming")
        st.write("- Embedded C")
        st.write("- ARM Microcontrollers")