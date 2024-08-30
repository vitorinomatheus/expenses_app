from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatEmotional(CategoriesBase, Base):
    __tablename__ = "CategoryEmotional"

    @classmethod
    def get_json_schema(cls) -> SQLAlchemyAutoSchema:
        return CatEmotionalJsonSchema()

class CatEmotionalJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatEmotional
        include_fk = True
        load_instance = True