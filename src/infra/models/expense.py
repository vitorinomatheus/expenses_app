from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class Expense(Base):
    __tablename__ = "Expense"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[float]
    user_id = mapped_column(ForeignKey("User.id"))
    cat_expense = mapped_column(ForeignKey("CategoryExpenseType.id"))
    cat_emotional = mapped_column(ForeignKey("CategoryEmotional.id"))
    cat_social = mapped_column(ForeignKey("CategorySocial.id"))
    cat_expense_feel = mapped_column(ForeignKey("CategoryExpenseFeel.id"))
    cat_budget_impact = mapped_column(ForeignKey("CategoryBudgetImpact.id"))

    def graphql_schema() -> str:
        return """
        
        """
        pass
