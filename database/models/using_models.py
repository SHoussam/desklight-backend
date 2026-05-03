from typing import Optional
from datetime import date as date_type, time as time_type
from sqlmodel import SQLModel


class TaskCreate(SQLModel):
    title: str
    module: str
    due_date: Optional[date_type] = None


class TaskRead(SQLModel):
    id: Optional[int] = None
    title: str
    module: str
    due_date: Optional[date_type] = None
    completed: bool


class TaskUpdate(SQLModel):
    title: Optional[str] = None
    module: Optional[str] = None
    due_date: Optional[date_type] = None
    completed: Optional[bool] = None


# ======================
# STUDY MODULE
# ======================


class StudyModuleCreate(SQLModel):
    name: str
    confidence: str
    progress: int
    exam_date: Optional[date_type] = None


class StudyModuleRead(SQLModel):
    id: Optional[int] = None
    name: str
    confidence: str
    progress: int
    exam_date: Optional[date_type] = None


class StudyModuleUpdate(SQLModel):
    name: Optional[str] = None
    confidence: Optional[str] = None
    progress: Optional[int] = None
    exam_date: Optional[date_type] = None


# ======================
# SCHEDULE EVENT
# ======================


class ScheduleEventCreate(SQLModel):
    title: str
    date: date_type
    time: Optional[time_type] = None
    category: str
    notes: Optional[str] = None


class ScheduleEventRead(SQLModel):
    id: Optional[int] = None
    title: str
    date: date_type
    time: Optional[time_type] = None
    category: str
    notes: Optional[str] = None


class ScheduleEventUpdate(SQLModel):
    title: Optional[str] = None
    date: Optional[date_type] = None
    time: Optional[time_type] = None
    category: Optional[str] = None
    notes: Optional[str] = None


# ======================
# EXPENSE
# ======================


class ExpenseCreate(SQLModel):
    name: str
    amount: float
    category: str
    date: date_type


class ExpenseRead(SQLModel):
    id: Optional[int] = None
    name: str
    amount: float
    category: str
    date: date_type


class ExpenseUpdate(SQLModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    date: Optional[date_type] = None


# ======================
# MOOD ENTRY
# ======================


class MoodEntryCreate(SQLModel):
    mood: str
    energy: int
    stress: int
    sleep: float
    note: Optional[str] = None
    date: date_type


class MoodEntryRead(SQLModel):
    id: Optional[int] = None
    mood: str
    energy: int
    stress: int
    sleep: float
    note: Optional[str] = None
    date: date_type


class MoodEntryUpdate(SQLModel):
    mood: Optional[str] = None
    energy: Optional[int] = None
    stress: Optional[int] = None
    sleep: Optional[float] = None
    note: Optional[str] = None
    date: Optional[date_type] = None


# ======================
# JOURNAL ENTRY
# ======================


class JournalEntryCreate(SQLModel):
    title: str
    mood: Optional[str] = None
    category: str
    text: str
    date: date_type


class JournalEntryRead(SQLModel):
    id: Optional[int] = None
    title: str
    mood: Optional[str] = None
    category: str
    text: str
    date: date_type


class JournalEntryUpdate(SQLModel):
    title: Optional[str] = None
    mood: Optional[str] = None
    category: Optional[str] = None
    text: Optional[str] = None
    date: Optional[date_type] = None


# ======================
# APP SETTINGS
# ======================


class AppSettingsRead(SQLModel):
    id: Optional[int] = None
    user_name: str
    dashboard_title: str
    currency: str
    tone: str
    theme: str


class AppSettingsUpdate(SQLModel):
    user_name: Optional[str] = None
    dashboard_title: Optional[str] = None
    currency: Optional[str] = None
    tone: Optional[str] = None
    theme: Optional[str] = None


# ======================
# AUTH
# ======================


class LoginSchema(SQLModel):
    email: str
    password: str


class SignupSchema(SQLModel):
    name: str
    email: str
    password: str
