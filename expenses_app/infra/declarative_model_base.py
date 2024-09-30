from sqlalchemy.orm import DeclarativeBase, class_mapper
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from abc import abstractmethod

class BaseModelColumnSchema:
    def __init__(self, name: str, type: str, nullable: bool, only_mutation: bool):
        self.name = name
        self.type = type
        self.nullable = nullable
        self.only_mutation = only_mutation

class BaseModel(DeclarativeBase):

    error: str
    ignore_list: bool = False

    @abstractmethod
    def get_json_schema(self) -> SQLAlchemyAutoSchema:
        pass

    @classmethod
    def get_class_map(cls):
        return class_mapper(cls)

    @classmethod
    def get_schema(cls) -> list[BaseModelColumnSchema]:
        """
        Generate list with information from database model columns.\n 
        Each column is represented as a BaseModelColumnSchema object
        """
        column_info = []

        mapped = cls.get_class_map()

        for value in mapped.columns:
            column = BaseModelColumnSchema(value.name, value.type.__visit_name__, value.nullable, value.name == "password")
            column_info.append(column)
        
        column_info.append(BaseModelColumnSchema("error", "string", True, False))

        return column_info