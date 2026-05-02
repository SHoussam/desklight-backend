from fastapi import APIRouter, Depends
from database.models.models import User, StudyModule
from database.models.using_models import StudyModuleCreate, StudyModuleRead, StudyModuleUpdate
from securety import get_current_user
from sqlmodel import Session, select
from database.conection import get_session

router = APIRouter()


@router.get("/study-modules/")
def get_study_modules(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(StudyModule).where(StudyModule.user_id == current_user.id)
    modules = session.exec(statement).all()
    modules = [StudyModuleRead.from_orm(module) for module in modules]
    return modules


@router.post("/study-modules/")
def create_study_module(
    module_in: StudyModuleCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_module = StudyModule.model_validate(module_in, update={"user_id": current_user.id})
    
    session.add(db_module)
    session.commit()
    session.refresh(db_module)
    
    return {
        "message": "Study module created successfully",
        "module_id": db_module.id
    }


@router.put("/study-modules/{module_id}")
def update_study_module(
    module_id: int,
    updated_module: StudyModuleUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(StudyModule).where(StudyModule.id == module_id, StudyModule.user_id == current_user.id)
    module_item = session.exec(statement).first()
    if not module_item:
        return {"error": "Study module not found"}
    
    if updated_module.name is not None:
        module_item.name = updated_module.name
    if updated_module.confidence is not None:
        module_item.confidence = updated_module.confidence
    if updated_module.progress is not None:
        module_item.progress = updated_module.progress
    if updated_module.exam_date is not None:
        module_item.exam_date = updated_module.exam_date
    
    session.add(module_item)
    session.commit()
    session.refresh(module_item)
    
    return {
        "message": "Study module updated successfully",
        "module_id": module_item.id
    }


@router.delete("/study-modules/{module_id}")
def delete_study_module(
    module_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(StudyModule).where(StudyModule.id == module_id, StudyModule.user_id == current_user.id)
    module_item = session.exec(statement).first()
    if not module_item:
        return {"error": "Study module not found"}
    
    session.delete(module_item)
    session.commit()
    
    return {
        "message": "Study module deleted successfully",
        "module_id": module_id
    }
