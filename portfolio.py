import streamlit as st
from src.pages import home, projects, skills_achievements, customize_profile, contact

def main():
    st.set_page_config(page_title="My Digital Footprint", layout="wide")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = ["Home", "Projects", "Skills & Achievements", "Customize Profile", "Contact"]
    selection = st.sidebar.radio("Go to", options)

    # Page selection
    if selection == "Home":
        home.display()
    elif selection == "Projects":
        projects.display()
    elif selection == "Skills & Achievements":
        skills_achievements.display()
    elif selection == "Customize Profile":
        customize_profile.display()
    elif selection == "Contact":
        contact.display()

if __name__ == "__main__":
    main()