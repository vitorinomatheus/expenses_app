from .categories_base import CategoriesBase 
from ...database import Base

class CatEmotional(CategoriesBase, Base):
    __tablename__ = "CategoryEmotional"