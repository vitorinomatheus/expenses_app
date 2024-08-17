from .categories_base import CategoriesBase 
from ...database import Base

class CatExpenseFeel(CategoriesBase, Base):
    __tablename__ = "CategoryExpenseFeel"