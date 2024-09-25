from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime

class Expense(Base):
    __tablename__ = "Expense"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[float]
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    cat_expense: Mapped[int] = mapped_column(ForeignKey("CategoryExpenseType.id"))
    cat_emotional: Mapped[int] = mapped_column(ForeignKey("CategoryEmotional.id"))
    cat_social: Mapped[int] = mapped_column(ForeignKey("CategorySocial.id"))
    cat_expense_feel: Mapped[int] = mapped_column(ForeignKey("CategoryExpenseFeel.id"))
    cat_budget_impact: Mapped[int] = mapped_column(ForeignKey("CategoryBudgetImpact.id"))
    date: Mapped[datetime]
    day_of_week: Mapped[int]
    month_week: Mapped[int]

    @classmethod
    def get_json_schema(cls) -> SQLAlchemyAutoSchema:
        return ExpenseJsonSchema()

class ExpenseJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
        include_relationship = True
        load_instance = True