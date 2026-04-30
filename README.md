# Project README

## Overview
This project provides user management and authentication features, including user signup and secure password handling. It is structured as a Python backend with API endpoints and database integration.

## Project Structure
- `securety.py`: Security utilities (e.g., password hashing).
- `api_root/user.py`: API endpoints for user operations (signup, user info, etc.).
- `database/conection.py`: Database connection setup.
- `database/models.py`: Database models (e.g., User schema).

## Features
- User signup with email and password
- Secure password hashing (bcrypt)
- API key generation for users
- MySQL database integration

## Requirements
- Python 3.8+
- FastAPI
- SQLModel
- Uvicorn
- bcrypt

## Setup
1. Install dependencies:
   ```bash
   pip install fastapi sqlmodel uvicorn bcrypt
   ```
2. Configure your database connection in `database/conection.py`.
3. Run the server:
   ```bash
   uvicorn api_root.user:app --reload
   ```

## Usage
- Access API endpoints at `http://localhost:8000/` after starting the server.
- Use `/signup/` to create a new user.

## License
This project is provided for educational purposes.
