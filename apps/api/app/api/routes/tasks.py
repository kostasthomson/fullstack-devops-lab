from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskRead

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)) -> Task:
    task = Task(title=payload.title, description=payload.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/", response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)) -> list[Task]:
    return db.query(Task).order_by(Task.id.asc()).all()