from fastapi import APIRouter, Depends
from database.models.models import User, AppSettings
from database.models.using_models import AppSettingsCreate, AppSettingsRead, AppSettingsUpdate
from securety import get_current_user
from sqlmodel import Session, select
from database.conection import get_session

router = APIRouter()


@router.get("/app-settings/")
def get_app_settings(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(AppSettings).where(AppSettings.user_id == current_user.id)
    settings = session.exec(statement).first()
    if settings:
        return AppSettingsRead.from_orm(settings)
    return {"error": "App settings not found"}


@router.post("/app-settings/")
def create_app_settings(
    settings_in: AppSettingsCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Check if settings already exist
    statement = select(AppSettings).where(AppSettings.user_id == current_user.id)
    existing_settings = session.exec(statement).first()
    if existing_settings:
        return {"error": "App settings already exist for this user"}
    
    db_settings = AppSettings.model_validate(settings_in, update={"user_id": current_user.id})
    
    session.add(db_settings)
    session.commit()
    session.refresh(db_settings)
    
    return {
        "message": "App settings created successfully",
        "settings_id": db_settings.id
    }


@router.put("/app-settings/{settings_id}")
def update_app_settings(
    settings_id: int,
    updated_settings: AppSettingsUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(AppSettings).where(AppSettings.id == settings_id, AppSettings.user_id == current_user.id)
    settings_item = session.exec(statement).first()
    if not settings_item:
        return {"error": "App settings not found"}
    
    if updated_settings.user_name is not None:
        settings_item.user_name = updated_settings.user_name
    if updated_settings.dashboard_title is not None:
        settings_item.dashboard_title = updated_settings.dashboard_title
    
    session.add(settings_item)
    session.commit()
    session.refresh(settings_item)
    
    return {
        "message": "App settings updated successfully",
        "settings_id": settings_item.id
    }


@router.delete("/app-settings/{settings_id}")
def delete_app_settings(
    settings_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(AppSettings).where(AppSettings.id == settings_id, AppSettings.user_id == current_user.id)
    settings_item = session.exec(statement).first()
    if not settings_item:
        return {"error": "App settings not found"}
    
    session.delete(settings_item)
    session.commit()
    
    return {
        "message": "App settings deleted successfully",
        "settings_id": settings_id
    }
