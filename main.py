from fastapi import FastAPI
from api_root.user import login_user, read_users_me, signup_user
from database.conection import create_db_and_tables
app = FastAPI()
create_db_and_tables()
app.add_api_route("/login", login_user, methods=["POST"])
app.add_api_route("/user", read_users_me, methods=["GET"])
app.add_api_route("/signup", signup_user, methods=["POST"])







