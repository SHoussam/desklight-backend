from fastapi import FastAPI
from database.conection import create_db_and_tables
from api_root import user, tasks_root, study_modules_root, schedule_events_root, expenses_root, mood_entries_root, journal_entries_root, app_settings_root

app = FastAPI()
create_db_and_tables()

# Include routers
app.include_router(user.router, prefix="/api", tags=["Auth & User"])
app.include_router(tasks_root.router, prefix="/api", tags=["Tasks"])
app.include_router(study_modules_root.router, prefix="/api", tags=["Study Modules"])
app.include_router(schedule_events_root.router, prefix="/api", tags=["Schedule Events"])
app.include_router(expenses_root.router, prefix="/api", tags=["Expenses"])
app.include_router(mood_entries_root.router, prefix="/api", tags=["Mood Entries"])
app.include_router(journal_entries_root.router, prefix="/api", tags=["Journal Entries"])
app.include_router(app_settings_root.router, prefix="/api", tags=["App Settings"])







