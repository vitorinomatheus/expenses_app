from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional

class UserAvrExpenseFeel:
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    expense_feel: Mapped[int] = mapped_column(ForeignKey("CategoryExpenseFeel.id"), nullable=True)
    value: Mapped[float]