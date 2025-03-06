def filter_projects_by_year(projects, year):
    return [project for project in projects if project['year'] == year]

def filter_projects_by_type(projects, project_type):
    return [project for project in projects if project['type'] == project_type]

def filter_projects_by_keyword(projects, keyword):
    return [project for project in projects if keyword.lower() in project['title'].lower() or keyword.lower() in project['description'].lower()]