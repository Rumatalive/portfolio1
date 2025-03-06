from streamlit import card, markdown, hyperlink

def project_card(title, project_type, description, code_link):
    with card():
        markdown(f"### {title}")
        markdown(f"**Type:** {project_type}")
        markdown(f"**Description:** {description}")
        if code_link:
            hyperlink("View Code", code_link)