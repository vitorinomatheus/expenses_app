from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from ..main import app

Base = declarative_base()

database_uri = app.config.get('SQLALCHEMY_DATABASE_URI')

engine = create_engine(database_uri)
