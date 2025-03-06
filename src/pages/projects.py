from streamlit import st
from src.utils.filters import filter_projects
from src.components.project_card import ProjectCard

# Sample project data
projects = [
    {
        "title": "Student Attendance System using Face Recognition",
        "type": "Individual",
        "description": "A system that automates attendance tracking using facial recognition technology.",
        "link": "https://github.com/username/student-attendance-system"
    },
    {
        "title": "E-commerce Website",
        "type": "Group",
        "description": "An online platform for buying and selling products, built using Flask and React.",
        "link": "https://github.com/username/ecommerce-website"
    },
    {
        "title": "Data Analysis of Sales Data",
        "type": "Class Assignment",
        "description": "Analyzed sales data to derive insights and trends using Python and Pandas.",
        "link": "https://github.com/username/sales-data-analysis"
    },
    {
        "title": "Final Year Project: Smart Home Automation",
        "type": "Dissertation",
        "description": "Developed a smart home system that allows users to control home appliances remotely.",
        "link": "https://github.com/username/smart-home-automation"
    }
]

# Project filtering options
project_types = ["All", "Year 1", "Group Projects", "Dissertation"]
selected_type = st.selectbox("Filter by Project Type", project_types)

# Filter projects based on selection
filtered_projects = filter_projects(projects, selected_type)

# Display projects
st.title("My Projects")
for project in filtered_projects:
    ProjectCard(
        title=project["title"],
        project_type=project["type"],
        description=project["description"],
        link=project["link"]
    )