from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional
from ...database import Base

class UserAvrExpenseFeel(Base):    
    __tablename__ = "user_avr_expense_feel"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    expense_feel: Mapped[int] = mapped_column(ForeignKey("CategoryExpenseFeel.id"), nullable=True)
    value: Mapped[float]

    ignore_list = True