from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatSocial(CategoriesBase, Base):
    __tablename__ = "CategorySocial"

class CatSocialJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatSocial
        include_fk = True
        load_instance = True