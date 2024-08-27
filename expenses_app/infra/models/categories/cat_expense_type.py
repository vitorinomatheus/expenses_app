from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatExpenseType(CategoriesBase, Base):
    __tablename__ = "CategoryExpenseType"

class CatExpenseTypeJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatExpenseType
        include_fk = True
        load_instance = True