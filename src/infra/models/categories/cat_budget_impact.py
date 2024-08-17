from .categories_base import CategoriesBase 
from ...database import Base

class CatBudgetImpact(CategoriesBase, Base):
        __tablename__ = "CategoryBudgetImpact"