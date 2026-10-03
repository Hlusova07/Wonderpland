from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models import TaskModel


app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")


class Task(BaseModel):
    title: str
    completed: bool = False


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_frontend():
    return FileResponse("frontend/index.html")


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).all()

    return [
        {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
        for task in tasks
    ]


@app.post("/tasks")
def create_task(
    task: Task,
    db: Session = Depends(get_db)
):
    new_task = TaskModel(
        title=task.title,
        completed=task.completed
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "id": new_task.id,
        "title": new_task.title,
        "completed": new_task.completed
    }


@app.patch("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: Task,
    db: Session = Depends(get_db)
):
    existing_task = db.query(TaskModel).filter(
        TaskModel.id == task_id
    ).first()

    if not existing_task:
        return {"error": "Задача не найдена"}

    existing_task.title = task.title
    existing_task.completed = task.completed

    db.commit()
    db.refresh(existing_task)

    return {
        "id": existing_task.id,
        "title": existing_task.title,
        "completed": existing_task.completed
    }


@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    existing_task = db.query(TaskModel).filter(
        TaskModel.id == task_id
    ).first()

    if not existing_task:
        return {"error": "Задача не найдена"}

    db.delete(existing_task)
    db.commit()

    return {"message": "Задача удалена"}