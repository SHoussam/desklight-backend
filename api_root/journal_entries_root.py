from fastapi import APIRouter, Depends
from database.models.models import User, JournalEntry
from database.models.using_models import JournalEntryCreate, JournalEntryRead, JournalEntryUpdate
from securety import get_current_user
from sqlmodel import Session, select
from database.conection import get_session

router = APIRouter()


@router.get("/journal-entries/")
def get_journal_entries(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(JournalEntry).where(JournalEntry.user_id == current_user.id)
    entries = session.exec(statement).all()
    entries = [JournalEntryRead.from_orm(entry) for entry in entries]
    return entries


@router.post("/journal-entries/")
def create_journal_entry(
    entry_in: JournalEntryCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_entry = JournalEntry.model_validate(entry_in, update={"user_id": current_user.id})
    
    session.add(db_entry)
    session.commit()
    session.refresh(db_entry)
    
    return {
        "message": "Journal entry created successfully",
        "entry_id": db_entry.id
    }


@router.put("/journal-entries/{entry_id}")
def update_journal_entry(
    entry_id: int,
    updated_entry: JournalEntryUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(JournalEntry).where(JournalEntry.id == entry_id, JournalEntry.user_id == current_user.id)
    entry_item = session.exec(statement).first()
    if not entry_item:
        return {"error": "Journal entry not found"}
    
    if updated_entry.title is not None:
        entry_item.title = updated_entry.title
    if updated_entry.mood is not None:
        entry_item.mood = updated_entry.mood
    if updated_entry.category is not None:
        entry_item.category = updated_entry.category
    if updated_entry.text is not None:
        entry_item.text = updated_entry.text
    if updated_entry.date is not None:
        entry_item.date = updated_entry.date
    
    session.add(entry_item)
    session.commit()
    session.refresh(entry_item)
    
    return {
        "message": "Journal entry updated successfully",
        "entry_id": entry_item.id
    }


@router.delete("/journal-entries/{entry_id}")
def delete_journal_entry(
    entry_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(JournalEntry).where(JournalEntry.id == entry_id, JournalEntry.user_id == current_user.id)
    entry_item = session.exec(statement).first()
    if not entry_item:
        return {"error": "Journal entry not found"}
    
    session.delete(entry_item)
    session.commit()
    
    return {
        "message": "Journal entry deleted successfully",
        "entry_id": entry_id
    }
