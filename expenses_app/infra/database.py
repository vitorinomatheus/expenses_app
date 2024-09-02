from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import current_app, g
from .declarative_model_base import BaseModel
from ..constants import *

Base = BaseModel

class Database:
    def __init__(self):
        self.database_uri = current_app.config.get('SQLALCHEMY_DATABASE_URI')
        self.engine = create_engine(self.database_uri, echo=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))
        
    
    def get_db(self):
        if DB not in g:
            g.db = self.session

        return g.db
    
    def close_db(e=None):
        db = g.pop(DB, None)

        if db is not None:
            db.close()

    def init_db(self):
        Base.metadata.create_all(bind=self.engine)
        db = self.get_db()
