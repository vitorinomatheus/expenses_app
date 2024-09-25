from flask import g
from .database import Database
from ..constants import *
from .declarative_model_base import BaseModel

class Repository:

    def get_list(self, model_class: BaseModel):
        db = self.get_db()
        data = db.session.query(model_class)
        json = model_class.get_json_schema() 
        response_list = [json.dump(d) for d in data]
        return response_list
    
    def get_filtered_list(self, model_class: BaseModel, filter_prop: str, filter_value):
        db = self.get_db()

        data = db.session.query(model_class).filter_by(filter_prop == filter_value)

        json = model_class.get_json_schema() 
        response_list = [json.dump(d) for d in data]

        return response_list
        
    def get_entity(self, model_class: BaseModel, id):
        db = self.get_db()

        data = db.session.query(model_class).filter_by(id=id).first()
        json = model_class.get_json_schema() 
        if data != None:
            return json.dump(data)
        else:
            raise Exception('Not Found')
        
    def save_entity(self, model_class: BaseModel):
        db = self.get_db()
        if (model_class.id == None):
            db.session.add(model_class)
        else:
            self.update_entity(model_class)
        db.session.commit()
        return model_class
    
    def update_entity(self, model_class: BaseModel):
        entity = self.get_entity(model_class, model_class.id)
        map = model_class.get_class_map().columns
        columns = [c.name for c in map]
        
        for key in columns:
            value = getattr(model_class, key, None)
            if value is not None:
                setattr(entity, key, value)
        

    def delete_entity(self, model_class: BaseModel, id: int):
        db = self.get_db()
        entity = self.get_entity(model_class, id)
        db.session.delete(entity)
        return True
    
    def get_db(self) -> Database:
        db = getattr(g, DB, None)
        if db is not None and db is Database:
            return db
        else:
            db = Database()
            db.init_db()
            return db
