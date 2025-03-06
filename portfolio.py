import streamlit as st
from src.pages import home, projects, skills_achievements, customize_profile, contact

def main():
    st.set_page_config(page_title="My Digital Footprint", layout="wide")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills & Achievements", "Customize Profile", "Contact"])

    # Page selection
    if page == "Home":
        home.show()
    elif page == "Projects":
        projects.show()
    elif page == "Skills & Achievements":
        skills_achievements.show()
    elif page == "Customize Profile":
        customize_profile.show()
    elif page == "Contact":
        contact.show()

if __name__ == "__main__":
    main()