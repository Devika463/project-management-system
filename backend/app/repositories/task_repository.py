from app.models.task import Task


def create_task(db, task_data):
    task = Task(**task_data.dict())

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_tasks(
    db,
    project_id=None,
    status=None,
    assigned_to=None,
    page=1,
    size=10
):
    query = db.query(Task)

    if project_id:
        query = query.filter(Task.project_id == project_id)

    if status:
        query = query.filter(Task.status == status)

    if assigned_to:
        query = query.filter(Task.assigned_to == assigned_to)

    return query.offset(
        (page - 1) * size
    ).limit(size).all()

def update_task_status(db, task_id, status):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        return None

    task.status = status

    db.commit()
    db.refresh(task)

    return task


def assign_task(db, task_id, assigned_to):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return None

    task.assigned_to = assigned_to

    db.commit()
    db.refresh(task)

    return task