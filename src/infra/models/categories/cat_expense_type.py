from .categories_base import CategoriesBase 
from ...database import Base

class CatExpenseType(CategoriesBase, Base):
    __tablename__ = "CategoryExpenseType"