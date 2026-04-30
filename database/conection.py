from database.models import create_engine, Session, SQLModel

# username: root, password: (empty), host: localhost, database: desklight_db
mysql_url = "mysql+pymysql://root:@localhost/desklight_db"

# Create the engine
engine = create_engine(mysql_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session