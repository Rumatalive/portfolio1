from streamlit import progress, container, markdown

def skill_bar(skill_name, skill_level):
    with container():
        markdown(f"**{skill_name}**")
        progress_bar = progress(skill_level)
        progress_bar.progress(skill_level)