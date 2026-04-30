
import os
from dotenv import load_dotenv
from database.models import create_engine, Session, SQLModel



load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))


mysql_url = os.getenv('DATABASE_URL')

engine = create_engine(mysql_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session(): 
    with Session(engine) as session:
        yield session