from sqlalchemy.orm import DeclarativeBase, class_mapper

class BaseModel(DeclarativeBase):
        
    @classmethod
    def get_schema(cls):
        column_info = []

        mapped = class_mapper(cls)

        for value in mapped.columns:
            column_name = value.name
            column_type = value.type
            column_nullable = value.nullable

            column_info.append((column_name, column_type, column_nullable))

        return column_info