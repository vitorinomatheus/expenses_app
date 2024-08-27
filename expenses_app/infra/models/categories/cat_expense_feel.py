from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatExpenseFeel(CategoriesBase, Base):
    __tablename__ = "CategoryExpenseFeel"

class CatExpenseFeelJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatExpenseFeel
        include_fk = True
        load_instance = True