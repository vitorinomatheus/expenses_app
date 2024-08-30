from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatExpenseFeel(CategoriesBase, Base):
    __tablename__ = "CategoryExpenseFeel"

    @classmethod
    def get_json_schema(cls) -> SQLAlchemyAutoSchema:
        return CatExpenseFeelJsonSchema()

class CatExpenseFeelJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatExpenseFeel
        include_fk = True
        load_instance = True