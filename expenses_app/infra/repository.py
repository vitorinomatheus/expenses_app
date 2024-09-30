from flask import g
from .database import Database
from ..constants import *
from .declarative_model_base import BaseModel
from .models.expense import Expense
from sqlalchemy.exc import SQLAlchemyError
from .models.user import User
from sqlalchemy.orm.attributes import flag_modified, set_attribute

class Repository:

    def get_list(self, model_class: BaseModel):
        try:
            db = self.get_db()
            data = db.session.query(type(model_class)).all()
            json = model_class.get_json_schema()
            response_list = [json.dump(d) for d in data]
            return response_list
        except SQLAlchemyError as e:
            model_class.error = f"Erro ao obter a lista: {str(e)}"
            json_error = model_class.get_json_schema().dump(model_class)
            return [json_error]
        except Exception as e:
            model_class.error = f"Erro inesperado: {str(e)}"
            json_error = model_class.get_json_schema().dump(model_class)
            return [json_error]
    
    def get_expense_by_user_id(self, expense: Expense, user_id):
        try:
            db = self.get_db()
            return db.session.query(type(expense)).filter_by(user_id = user_id).all()
        except SQLAlchemyError as e:
            expense.error = f"Erro ao obter a lista: {str(e)}"
            json_error = expense.get_json_schema().dump(expense)
            return [json_error]
        except Exception as e:
            expense.error = f"Erro inesperado: {str(e)}"
            json_error = expense.get_json_schema().dump(expense)
            return [json_error]
        
        
    def get_entity(self, model_class: BaseModel, id):
        try:
            db = self.get_db()
            data = db.session.query(type(model_class)).filter_by(id=id).first()
            json = model_class.get_json_schema() 
            if data != None:
                return_data = json.dump(data)

                return return_data
            else:
                raise Exception('Not Found')
        except SQLAlchemyError as e:
            model_class.error = f"Erro ao obter a lista: {str(e)}"
            json_error = model_class.get_json_schema().dump(model_class)
            return json_error
        except Exception as e:
            model_class.error = f"Erro inesperado: {str(e)}"
            json_error = model_class.get_json_schema().dump(model_class)
            return json_error
        
    def save_entity(self, model_class: BaseModel):
        try:
            db = self.get_db()
            if isinstance(model_class.id, str) and model_class.id:
                self.update_entity(model_class, db)
            else:
                db.session.add(model_class)
            db.session.commit()
            return model_class
        except SQLAlchemyError as e:
            model_class.error = f"Erro ao obter a lista: {str(e)}"
            return model_class
        except Exception as e:
            model_class.error = f"Erro inesperado: {str(e)}"
            return model_class
    
    def update_entity(self, model_class: BaseModel, db: Database) -> BaseModel:
        entity = db.session.query(type(model_class)).filter_by(id=model_class.id).first()
        map = model_class.get_class_map().columns
        columns = [c.name for c in map]
        
        for key in columns:
            value = getattr(model_class, key, None)
            if value is not None:
                setattr(entity, key, value)
                flag_modified(entity, key)
        
        return entity
        
    def delete_entity(self, model_class: BaseModel, id: int):
        try:
            db = self.get_db()
            entity = db.session.query(type(model_class)).filter_by(id=id).first()
            db.session.delete(entity)
            db.session.commit()
            return entity
        except SQLAlchemyError as e:
            model_class.error = f"Erro ao obter a lista: {str(e)}"
            return model_class
        except Exception as e:
            model_class.error = f"Erro inesperado: {str(e)}"
            return model_class
        
    def get_user_by_username(self, username: str):
        try:
            user = User()
            db = self.get_db()
            data = db.session.query(User).filter_by(email=username).first()
            return data
        except SQLAlchemyError as e:
            user.error = f"Erro ao obter a lista: {str(e)}"
            json_error = user.get_json_schema().dump(user)
            return json_error
        except Exception as e:
            user.error = f"Erro inesperado: {str(e)}"
            json_error = user.get_json_schema().dump(user)
            return json_error

    
    def get_db(self) -> Database:
        db = getattr(g, DB, None)
        if db is not None and db is Database:
            return db
        else:
            db = Database()
            db.init_db()
            return db