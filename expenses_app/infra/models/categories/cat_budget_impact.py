from .categories_base import CategoriesBase 
from ...database import Base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class CatBudgetImpact(CategoriesBase, Base):
    __tablename__ = "CategoryBudgetImpact"

    @classmethod
    def get_json_schema(cls) -> SQLAlchemyAutoSchema:
            return CatBudgetImpactJsonSchema()

class CatBudgetImpactJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CatBudgetImpact
        include_fk = True
        load_instance = True