from sqlmodel import create_engine, Session

from app.config import settings

engine = create_engine(settings.database_url, echo=True)

def get_session():
    """give a db session used by the Depends() in the routes"""
    with Session(engine) as session:
        yield session