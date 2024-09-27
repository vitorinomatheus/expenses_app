from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional
from ...database import Base

class UserAvrTimePeriod(Base):
    __tablename__ = "user_data_avr_time_period"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    month_week: Mapped[Optional[int]]
    week_day: Mapped[Optional[int]]
    value: Mapped[float]