from pathlib import Path
import streamlit as st

def home():
    # Load profile picture
    profile_picture = Path("src/assets/profile_picture.jpg")
    
    # Display profile picture
    st.image(profile_picture, width=150)
    
    # User details
    st.title("Your Full Name")
    st.subheader("Location, University")
    st.write("Field of Study: BSc Computer Science, Year 3")
    
    # Brief introduction
    st.write("""
    Brief Introduction: A summary of who you are and what excites you about technology.
    """)
    
    # Resume download button
    resume_file = Path("src/assets/resume.pdf")
    st.download_button("Download Resume", resume_file.read_bytes(), "resume.pdf")

if __name__ == "__main__":
    home()