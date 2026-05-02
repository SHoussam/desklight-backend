from fastapi import APIRouter , Depends
from database.models.models import  User ,Task
from database.models.using_models import TaskCreate , TaskRead , TaskUpdate
from securety import get_current_user
from sqlmodel import Session , select
from database.conection import get_session

router= APIRouter()



@router.get("/tasks/")
def get_tasks(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(Task).where(Task.user_id == current_user.id)
    tasks = session.exec(statement).all()
    tasks = [TaskRead.from_orm(task) for task in tasks]
    return tasks


@router.post("/tasks/")
def create_task(
    task_in: TaskCreate, 
    current_user: User = Depends(get_current_user), 
    session: Session = Depends(get_session)
):
    db_task = Task.model_validate(task_in, update={"user_id": current_user.id})
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    
    return {
        "message": "Task created successfully",
        "task_id": db_task.id
    }

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(Task).where(Task.id == task_id, Task.user_id == current_user.id)
    task_item = session.exec(statement).first()
    if not task_item:
        return {"error": "Task not found"}
    
    if updated_task.title is not None:
        task_item.title = updated_task.title
    if updated_task.module is not None:
        task_item.module = updated_task.module
    if updated_task.due_date is not None:
        task_item.due_date = updated_task.due_date
    if updated_task.completed is not None:
        task_item.completed = updated_task.completed
    
    session.add(task_item)
    session.commit()
    session.refresh(task_item)
    
    return {
        "message": "Task updated successfully",
        "task_id": task_item.id
    }


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user), session = Depends(get_session)):
    statement = select(Task).where(Task.id == task_id, Task.user_id == current_user.id)
    task_item = session.exec(statement).first()
    if not task_item:
        return {"error": "Task not found"}
    
    session.delete(task_item)
    session.commit()
    
    return {
        "message": "Task deleted successfully",
        "task_id": task_id
    }