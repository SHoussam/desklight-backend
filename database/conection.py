
from sqlmodel import create_engine, Session, SQLModel
from database.models import models
mysql_url = "mysql+pymysql://root:@localhost/desklight_db"

engine = create_engine(mysql_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session(): 
    with Session(engine) as session:
        yield session