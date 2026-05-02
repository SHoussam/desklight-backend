from fastapi import APIRouter, Depends
from database.models.models import User, MoodEntry
from database.models.using_models import MoodEntryCreate, MoodEntryRead, MoodEntryUpdate
from securety import get_current_user
from sqlmodel import Session, select
from database.conection import get_session

router = APIRouter()


@router.get("/mood-entries/")
def get_mood_entries(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(MoodEntry).where(MoodEntry.user_id == current_user.id)
    entries = session.exec(statement).all()
    entries = [MoodEntryRead.from_orm(entry) for entry in entries]
    return entries


@router.post("/mood-entries/")
def create_mood_entry(
    entry_in: MoodEntryCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_entry = MoodEntry.model_validate(entry_in, update={"user_id": current_user.id})
    
    session.add(db_entry)
    session.commit()
    session.refresh(db_entry)
    
    return {
        "message": "Mood entry created successfully",
        "entry_id": db_entry.id
    }


@router.put("/mood-entries/{entry_id}")
def update_mood_entry(
    entry_id: int,
    updated_entry: MoodEntryUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(MoodEntry).where(MoodEntry.id == entry_id, MoodEntry.user_id == current_user.id)
    entry_item = session.exec(statement).first()
    if not entry_item:
        return {"error": "Mood entry not found"}
    
    if updated_entry.mood is not None:
        entry_item.mood = updated_entry.mood
    if updated_entry.energy is not None:
        entry_item.energy = updated_entry.energy
    if updated_entry.stress is not None:
        entry_item.stress = updated_entry.stress
    if updated_entry.sleep is not None:
        entry_item.sleep = updated_entry.sleep
    if updated_entry.note is not None:
        entry_item.note = updated_entry.note
    if updated_entry.date is not None:
        entry_item.date = updated_entry.date
    
    session.add(entry_item)
    session.commit()
    session.refresh(entry_item)
    
    return {
        "message": "Mood entry updated successfully",
        "entry_id": entry_item.id
    }


@router.delete("/mood-entries/{entry_id}")
def delete_mood_entry(
    entry_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(MoodEntry).where(MoodEntry.id == entry_id, MoodEntry.user_id == current_user.id)
    entry_item = session.exec(statement).first()
    if not entry_item:
        return {"error": "Mood entry not found"}
    
    session.delete(entry_item)
    session.commit()
    
    return {
        "message": "Mood entry deleted successfully",
        "entry_id": entry_id
    }
