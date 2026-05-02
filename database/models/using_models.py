from sqlmodel import  SQLModel 
from datetime import date , time



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
    title: str | None = None
    module: str | None = None
    due_date: date | None = None
    completed: bool | None = None


# ======================
# STUDY MODULE
# ======================
class StudyModuleCreate(SQLModel):
    name: str
    confidence: str
    progress: int
    exam_date: date | None = None


class StudyModuleRead(SQLModel):
    id: int | None
    name: str
    confidence: str
    progress: int
    exam_date: date | None = None


class StudyModuleUpdate(SQLModel):
    name: str | None = None
    confidence: str | None = None
    progress: int | None = None
    exam_date: date | None = None


# ======================
# SCHEDULE EVENT
# ======================
class ScheduleEventCreate(SQLModel):
    title: str
    date: date
    time: time | None = None
    category: str
    notes: str | None = None


class ScheduleEventRead(SQLModel):
    id: int | None
    title: str
    date: date
    time: time | None
    category: str
    notes: str | None = None


class ScheduleEventUpdate(SQLModel):
    title: str | None = None
    date: date | None = None
    time: time | None = None
    category: str | None = None
    notes: str | None = None


# ======================
# EXPENSE
# ======================
class ExpenseCreate(SQLModel):
    name: str
    amount: float
    category: str
    date: date


class ExpenseRead(SQLModel):
    id: int | None
    name: str
    amount: float
    category: str
    date: date


class ExpenseUpdate(SQLModel):
    name: str | None = None
    amount: float | None = None
    category: str | None = None
    date: date | None = None


# ======================
# MOOD ENTRY
# ======================
class MoodEntryCreate(SQLModel):
    mood: str
    energy: int
    stress: int
    sleep: float
    note: str | None = None
    date: date


class MoodEntryRead(SQLModel):
    id: int | None
    mood: str
    energy: int
    stress: int
    sleep: float
    note: str | None = None
    date: date


class MoodEntryUpdate(SQLModel):
    mood: str | None = None
    energy: int | None = None
    stress: int | None = None
    sleep: float | None = None
    note: str | None = None
    date: date | None = None


# ======================
# JOURNAL ENTRY
# ======================
class JournalEntryCreate(SQLModel):
    title: str
    mood: str | None = None
    category: str
    text: str
    date: date


class JournalEntryRead(SQLModel):
    id: int | None
    title: str
    mood: str | None = None
    category: str
    text: str
    date: date


class JournalEntryUpdate(SQLModel):
    title: str | None = None
    mood: str | None = None
    category: str | None = None
    text: str | None = None
    date: date | None = None


# ======================
# APP SETTINGS
# ======================

class AppSettingsRead(SQLModel):
    user_name: str 
    dashboard_title: str
    currency: str
    tone: str
    theme: str

class AppSettingsUpdate(SQLModel):
    dashboard_title: str | None = None
    currency: str | None = None
    tone: str | None = None
    theme: str | None = None
# ======================

class LoginSchema(SQLModel):
    email: str
    password: str

class SignupSchema(SQLModel):
    name: str
    email: str
    password: str