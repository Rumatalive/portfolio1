import streamlit as st

def customize_profile():
    st.title("Customize Your Profile")

    # Input fields for profile customization
    name = st.text_input("Full Name", value="", placeholder="Enter your full name")
    bio = st.text_area("Bio", value="", placeholder="Write a brief bio about yourself")
    
    # Skill input fields
    skills = st.text_input("Skills", value="", placeholder="Enter your skills separated by commas")

    # Save button
    if st.button("Save Changes"):
        # Here you would typically save the changes to a database or local storage
        st.success("Profile updated successfully!")

    # Optionally, load existing profile data if available
    # This could be implemented with local storage or a database connection

if __name__ == "__main__":
    customize_profile()