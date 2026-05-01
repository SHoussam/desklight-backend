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
- `POST /login` — User login (returns API key)
- `POST /signup` — User registration
- `GET /user` — Get current user info (requires API key)

### Tasks
- `GET /tasks` — List all tasks for current user
- `POST /tasks` — Create a new task
- `PUT /tasks/{task_id}` — Update a task
- `DELETE /tasks/{task_id}` — Delete a task

## Database Models

- **User**: id, name, email, password, api_key
- **Task**: id, user_id, title, module, due_date, completed
- **StudyModule, ScheduleEvent, Expense, MoodEntry, JournalEntry, AppSettings**: See `database/models/models.py` for full details

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