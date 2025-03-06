from streamlit import st
from components.skill_bar import skill_bar

def skills_achievements():
    st.title("Skills & Achievements")

    st.subheader("Programming Languages")
    skill_bar("Python", 90)
    skill_bar("JavaScript", 75)
    skill_bar("SQL", 80)

    st.subheader("Machine Learning / Data Science")
    skill_bar("Machine Learning", 70)
    skill_bar("Data Analysis", 85)

    st.subheader("Web Development")
    skill_bar("HTML", 90)
    skill_bar("CSS", 80)
    skill_bar("React", 70)
    skill_bar("Flask", 75)

    st.subheader("Certifications & Achievements")
    achievements = [
        "Completed Google Data Analytics Certification",
        "Coding Finalist at XYZ University",
        "Participated in Hackathon 2023",
        "Completed Internship at ABC Tech"
    ]
    
    for achievement in achievements:
        st.write(f"- {achievement}")

if __name__ == "__main__":
    skills_achievements()