from fastapi import APIRouter, Depends
from database.models.models import User, ScheduleEvent
from database.models.using_models import ScheduleEventCreate, ScheduleEventRead, ScheduleEventUpdate
from securety import get_current_user
from sqlmodel import Session, select
from database.conection import get_session

router = APIRouter()


@router.get("/schedule-events/")
def get_schedule_events(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(ScheduleEvent).where(ScheduleEvent.user_id == current_user.id)
    events = session.exec(statement).all()
    eventse = [ScheduleEventRead.from_orm(event) for event in events]
    return eventse


@router.post("/schedule-events/")
def create_schedule_event(
    event_in: ScheduleEventCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_event = ScheduleEvent.model_validate(event_in, update={"user_id": current_user.id})
    
    session.add(db_event)
    session.commit()
    session.refresh(db_event)
    
    return {
        "message": "Schedule event created successfully",
        "event_id": db_event.id
    }


@router.put("/schedule-events/{event_id}")
def update_schedule_event(
    event_id: int,
    updated_event: ScheduleEventUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(ScheduleEvent).where(ScheduleEvent.id == event_id, ScheduleEvent.user_id == current_user.id)
    event_item = session.exec(statement).first()
    if not event_item:
        return {"error": "Schedule event not found"}
    
    if updated_event.title is not None:
        event_item.title = updated_event.title
    if updated_event.date is not None:
        event_item.date = updated_event.date
    if updated_event.time is not None:
        event_item.time = updated_event.time
    if updated_event.category is not None:
        event_item.category = updated_event.category
    if updated_event.notes is not None:
        event_item.notes = updated_event.notes
    
    session.add(event_item)
    session.commit()
    session.refresh(event_item)
    
    return {
        "message": "Schedule event updated successfully",
        "event_id": event_item.id
    }


@router.delete("/schedule-events/{event_id}")
def delete_schedule_event(
    event_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(ScheduleEvent).where(ScheduleEvent.id == event_id, ScheduleEvent.user_id == current_user.id)
    event_item = session.exec(statement).first()
    if not event_item:
        return {"error": "Schedule event not found"}
    
    session.delete(event_item)
    session.commit()
    
    return {
        "message": "Schedule event deleted successfully",
        "event_id": event_id
    }
