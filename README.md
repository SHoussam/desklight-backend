# DeskLight Backend

This is the backend for the DeskLight project, built with FastAPI and SQLModel. It provides RESTful API endpoints for user authentication, task management, and more, with MySQL as the database backend.

## Project Structure

- `main.py` — FastAPI app entry point and route registration
- `api_root/` — API endpoint logic (user and task routes)
- `database/` — Database connection and all data models
    - `models/` — User, Task, StudyModule, ScheduleEvent, Expense, MoodEntry, JournalEntry, AppSettings schemas
- `securety.py` — Security and authentication utilities

## Features

- User registration, login, and authentication (API key based)
- Task CRUD (create, read, update, delete) for authenticated users
- Extensible models for study modules, schedules, expenses, moods, journals, and app settings
- MySQL database integration via SQLModel

## API Endpoints

### Auth & User
- `POST /api/login/` — User login (returns API key)
- `POST /api/signup/` — User registration
- `GET /api/user/` — Get current user info (requires API key)

### Tasks
- `GET /api/tasks/` — List all tasks for current user
- `POST /api/tasks/` — Create a new task
- `PUT /api/tasks/{task_id}` — Update a task
- `DELETE /api/tasks/{task_id}` — Delete a task

### Study Modules
- `GET /api/study-modules/` — List all study modules for current user
- `POST /api/study-modules/` — Create a new study module
- `PUT /api/study-modules/{module_id}` — Update a study module
- `DELETE /api/study-modules/{module_id}` — Delete a study module

### Schedule Events
- `GET /api/schedule-events/` — List all schedule events for current user
- `POST /api/schedule-events/` — Create a new schedule event
- `PUT /api/schedule-events/{event_id}` — Update a schedule event
- `DELETE /api/schedule-events/{event_id}` — Delete a schedule event

### Expenses
- `GET /api/expenses/` — List all expenses for current user
- `POST /api/expenses/` — Create a new expense
- `PUT /api/expenses/{expense_id}` — Update an expense
- `DELETE /api/expenses/{expense_id}` — Delete an expense

### Mood Entries
- `GET /api/mood-entries/` — List all mood entries for current user
- `POST /api/mood-entries/` — Create a new mood entry
- `PUT /api/mood-entries/{entry_id}` — Update a mood entry
- `DELETE /api/mood-entries/{entry_id}` — Delete a mood entry

### Journal Entries
- `GET /api/journal-entries/` — List all journal entries for current user
- `POST /api/journal-entries/` — Create a new journal entry
- `PUT /api/journal-entries/{entry_id}` — Update a journal entry
- `DELETE /api/journal-entries/{entry_id}` — Delete a journal entry

### App Settings
- `GET /api/app-settings/` — Get app settings for current user
- `PUT /api/app-settings/` — Update app settings
## Database Models

- **User**: id, name, email, password, api_key
- **Task**: id, user_id, title, module, due_date, completed
- **StudyModule**: id, user_id, name, confidence, progress (0-100), exam_date
- **ScheduleEvent**: id, user_id, title, date, time, category, notes
- **Expense**: id, user_id, name, amount, category, date
- **MoodEntry**: id, user_id, mood, energy (0-100), stress (0-100), sleep (hours), note, date
- **JournalEntry**: id, user_id, title, mood, category, text, date
- **AppSettings**: id, user_id, user_name, dashboard_title

## Getting Started

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Ensure MySQL is running and update the connection string in `database/conection.py` if needed
5. Run the server: `uvicorn main:app --reload`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
