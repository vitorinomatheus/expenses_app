from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional

class UserAvrExpenseType:
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    expense_type: Mapped[int] = mapped_column(ForeignKey("CategoryExpenseType.id"), nullable=True)
    value: Mapped[float]