from fastapi import APIRouter, Depends
from database.models.models import User, AppSettings
from database.models.using_models import  AppSettingsRead, AppSettingsUpdate
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




@router.put("/app-settings/")
def update_app_settings(
    updated_settings: AppSettingsUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(AppSettings).where(AppSettings.user_id == current_user.id)
    settings_item = session.exec(statement).first()
    if not settings_item:
        return {"error": "App settings not found"}

    if updated_settings.dashboard_title is not None:
        settings_item.dashboard_title = updated_settings.dashboard_title
    if updated_settings.currency is not None:
        settings_item.currency = updated_settings.currency
    if updated_settings.tone is not None:
        settings_item.tone = updated_settings.tone
    if updated_settings.theme is not None:
        settings_item.theme = updated_settings.theme

    session.add(settings_item)
    session.commit()
    session.refresh(settings_item)
    
    return {
        "message": "App settings updated successfully",
        "settings_id": settings_item.id
    }


