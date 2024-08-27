from sqlalchemy.orm import DeclarativeBase, class_mapper

class BaseModelColumnSchema:
    def __init__(self, name: str, type: str, nullable: bool):
        self.name = name
        self.type = type
        self.nullable = nullable

class BaseModel(DeclarativeBase):
        
    @classmethod
    def get_schema(cls) -> list[BaseModelColumnSchema]:
        """
        Generate list with information from database model columns.\n 
        Each column is represented as a BaseModelColumnSchema object
        """
        column_info = []

        mapped = class_mapper(cls)

        for value in mapped.columns:
            column = BaseModelColumnSchema(value.name, value.type.__visit_name__, value.nullable)
            column_info.append(column)

        return column_info