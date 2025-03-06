import streamlit as st

def contact_page():
    st.title("Contact Me")
    
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            # Here you would typically handle the form submission, e.g., send an email or save to a database
            st.success("Thank you for your message! I'll get back to you soon.")
    
    st.subheader("Connect with Me")
    st.write("Feel free to reach out through my social media:")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/your-profile)")
    st.markdown("[GitHub](https://github.com/your-username)")
    st.markdown("[Portfolio Website](https://your-portfolio-website.com)")
    st.markdown("Email: [your-email@example.com](mailto:your-email@example.com)")

if __name__ == "__main__":
    contact_page()