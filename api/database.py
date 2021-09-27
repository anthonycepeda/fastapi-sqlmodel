from sqlmodel import Session, SQLModel, create_engine
from api.config import settings


connect_args = {"check_same_thread": False}
engine = create_engine(settings.DATABASE_URI, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
