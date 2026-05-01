from fastapi import FastAPI
from api_root.user import login_user, read_users_me, signup_user
from database.conection import create_db_and_tables
from api_root.tasks_root import get_tasks, create_task, update_task, delete_task
app = FastAPI()
create_db_and_tables()
app.add_api_route("/login", login_user, methods=["POST"])
app.add_api_route("/user", read_users_me, methods=["GET"])
app.add_api_route("/signup", signup_user, methods=["POST"])
app.add_api_route("/tasks", get_tasks, methods=["GET"])
app.add_api_route("/tasks", create_task, methods=["POST"])
app.add_api_route("/tasks/{task_id}", update_task, methods=["PUT"])
app.add_api_route("/tasks/{task_id}", delete_task, methods=["DELETE"])







