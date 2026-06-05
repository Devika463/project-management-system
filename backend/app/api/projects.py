from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.roles import require_admin

from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate
)

from app.repositories.project_repository import (
    create_project,
    get_projects,
    update_project,
    delete_project
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/")
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return create_project(db, project)


@router.get("/", response_model=list[ProjectResponse])
def list_projects(
    db: Session = Depends(get_db)
):
    return get_projects(db)


@router.put("/{project_id}")
def edit_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    updated_project = update_project(
        db,
        project_id,
        project
    )

    if not updated_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return updated_project


@router.delete("/{project_id}")
def remove_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    project = delete_project(
        db,
        project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project deleted successfully"
    }