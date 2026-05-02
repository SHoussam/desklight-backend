from sqlmodel import  SQLModel 
from datetime import date
from typing import Optional



class TaskCreate(SQLModel):
    title: str
    module: str
    due_date: date


class TaskRead(SQLModel):
    title: str
    module: str
    due_date: date
    completed: bool



class TaskUpdate(SQLModel):
    title: Optional[str] = None
    module: Optional[str] = None
    due_date: Optional[date] = None
    completed: Optional[bool] = None


# ======================
# STUDY MODULE
# ======================
class StudyModuleCreate(SQLModel):
    name: str
    confidence: str
    progress: int
    exam_date: Optional[date] = None


class StudyModuleRead(SQLModel):
    id: Optional[int]
    name: str
    confidence: str
    progress: int
    exam_date: Optional[date] = None


class StudyModuleUpdate(SQLModel):
    name: Optional[str] = None
    confidence: Optional[str] = None
    progress: Optional[int] = None
    exam_date: Optional[date] = None


# ======================
# SCHEDULE EVENT
# ======================
class ScheduleEventCreate(SQLModel):
    title: str
    date: date
    time: Optional[str] = None
    category: str
    notes: Optional[str] = None


class ScheduleEventRead(SQLModel):
    id: Optional[int]
    title: str
    date: date
    time: Optional[str] = None
    category: str
    notes: Optional[str] = None


class ScheduleEventUpdate(SQLModel):
    title: Optional[str] = None
    date: Optional[date] = None
    time: Optional[str] = None
    category: Optional[str] = None
    notes: Optional[str] = None


# ======================
# EXPENSE
# ======================
class ExpenseCreate(SQLModel):
    name: str
    amount: float
    category: str
    date: date


class ExpenseRead(SQLModel):
    id: Optional[int]
    name: str
    amount: float
    category: str
    date: date


class ExpenseUpdate(SQLModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    date: Optional[date] = None


# ======================
# MOOD ENTRY
# ======================
class MoodEntryCreate(SQLModel):
    mood: str
    energy: int
    stress: int
    sleep: float
    note: Optional[str] = None
    date: date


class MoodEntryRead(SQLModel):
    id: Optional[int]
    mood: str
    energy: int
    stress: int
    sleep: float
    note: Optional[str] = None
    date: date


class MoodEntryUpdate(SQLModel):
    mood: Optional[str] = None
    energy: Optional[int] = None
    stress: Optional[int] = None
    sleep: Optional[float] = None
    note: Optional[str] = None
    date: Optional[date] = None


# ======================
# JOURNAL ENTRY
# ======================
class JournalEntryCreate(SQLModel):
    title: str
    mood: Optional[str] = None
    category: str
    text: str
    date: date


class JournalEntryRead(SQLModel):
    id: Optional[int]
    title: str
    mood: Optional[str] = None
    category: str
    text: str
    date: date


class JournalEntryUpdate(SQLModel):
    title: Optional[str] = None
    mood: Optional[str] = None
    category: Optional[str] = None
    text: Optional[str] = None
    date: Optional[date] = None


# ======================
# APP SETTINGS
# ======================
class AppSettingsCreate(SQLModel):
    user_name: str
    dashboard_title: str


class AppSettingsRead(SQLModel):
    id: Optional[int]
    user_name: str
    dashboard_title: str


class AppSettingsUpdate(SQLModel):
    user_name: Optional[str] = None
    dashboard_title: Optional[str] = None
# ======================