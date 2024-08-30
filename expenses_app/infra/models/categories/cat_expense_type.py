from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatExpenseType(CategoriesBase, Base):
    __tablename__ = "CategoryExpenseType"

    @classmethod
    def get_json_schema(cls) -> SQLAlchemyAutoSchema:
        return CatExpenseTypeJsonSchema()

class CatExpenseTypeJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatExpenseType
        include_fk = True
        load_instance = True