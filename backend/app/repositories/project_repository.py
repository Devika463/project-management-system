from app.models.project import Project
from app.models.task import Task
def create_project(db, project_data):
    project = Project(**project_data.dict())

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_projects(db):
    return db.query(Project).all()

def update_project(db, project_id, project_data):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return None

    project.name = project_data.name
    project.description = project_data.description

    db.commit()
    db.refresh(project)

    return project

def delete_project(db, project_id):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        return None

    db.delete(project)
    db.commit()

    return project