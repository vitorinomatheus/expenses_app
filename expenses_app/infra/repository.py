from flask import g
from .database import Database
from ..constants import *
from .declarative_model_base import BaseModel

class Repository:

    def get_list(self, model_class: BaseModel):
        db = self.get_db()
        return db.query(model_class)
        
    def get_entity(self, model_class: BaseModel, id):
        db = self.get_db()
        data = db.session.query(model_class).all()
        json = model_class.get_json_schema() 
        for d in data:
            teste = json.dump(d)
        return teste
    
    def get_db(self) -> Database:
        db = getattr(g, DB, None)
        if db is not None and db is Database:
            return db
        else:
            database = Database()
            database.init_db()
            return database
