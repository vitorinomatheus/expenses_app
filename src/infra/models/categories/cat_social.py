from .categories_base import CategoriesBase 
from ...database import Base

class CatSocial(CategoriesBase, Base):
    __tablename__ = "CategorySocial"