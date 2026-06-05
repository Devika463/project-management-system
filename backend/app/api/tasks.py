from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.schemas.task import (
    TaskCreate,
    TaskStatusUpdate,
    TaskAssign
)

from app.repositories.task_repository import (
    create_task,
    get_tasks,
    update_task_status,
    assign_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_task(db, task)


@router.get("/")
def list_tasks(
    project_id: int = None,
    status: str = None,
    assigned_to: int = None,
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db)
):
    return get_tasks(
        db,
        project_id,
        status,
        assigned_to,
        page,
        size
    )


@router.patch("/{task_id}/status")
def change_status(
    task_id: int,
    data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = update_task_status(
        db,
        task_id,
        data.status
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.patch("/{task_id}/assign")
def assign_task_to_user(
    task_id: int,
    data: TaskAssign,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = assign_task(
        db,
        task_id,
        data.assigned_to
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task