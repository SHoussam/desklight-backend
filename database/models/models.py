from typing import Optional
from datetime import date as date_type, time as time_type
from sqlmodel import Field, SQLModel


# ======================
# USER
# ======================
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str
    api_key: Optional[str] = None


# ======================
# TASKS
# ======================
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    title: str
    module: str
    due_date: Optional[date_type] = None
    completed: bool = Field(default=False)


# STUDY MODULES
# ======================
class StudyModule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    name: str
    confidence: str  # you can later convert to Enum
    progress: int  # percentage (0–100)
    exam_date: Optional[date_type] = None


# ======================
# SCHEDULE EVENTS
# ======================
class ScheduleEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    title: str
    date: date_type
    time: Optional[time_type] = None
    category: str
    notes: Optional[str] = None


# ======================
# EXPENSES
# ======================
class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    name: str
    amount: float
    category: str
    date: date_type


# ======================
# MOOD ENTRIES
# ======================
class MoodEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    mood: str
    energy: int  # 0–100
    stress: int  # 0–100
    sleep: float  # hours
    note: Optional[str] = None
    date: date_type


# ======================
# JOURNAL ENTRIES
# ======================
class JournalEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    title: str
    mood: Optional[str] = None
    category: str
    text: str
    date: date_type


# ======================
# APP SETTINGS
# ======================
class AppSettings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")

    user_name: str
    dashboard_title: str
    currency: str
    tone: str
    theme: str
