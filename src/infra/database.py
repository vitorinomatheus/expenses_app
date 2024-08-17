from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import config
from .declarative_model_base import BaseModel

Base = BaseModel

database_uri = config.Config['SQLALCHEMY_DATABASE_URI']

# engine = create_engine(database_uri)
