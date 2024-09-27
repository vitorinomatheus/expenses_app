from sqlalchemy.orm import DeclarativeBase, class_mapper
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from abc import abstractmethod

class BaseModelColumnSchema:
    def __init__(self, name: str, type: str, nullable: bool):
        self.name = name
        self.type = type
        self.nullable = nullable

class BaseModel(DeclarativeBase):

    error: str

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
            column = BaseModelColumnSchema(value.name, value.type.__visit_name__, value.nullable)
            column_info.append(column)

        return column_info