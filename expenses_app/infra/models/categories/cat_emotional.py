from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatEmotional(CategoriesBase, Base):
    __tablename__ = "CategoryEmotional"

class CatEmotionalJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatEmotional
        include_fk = True
        load_instance = True