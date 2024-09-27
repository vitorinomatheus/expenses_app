from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional
from ...database import Base

class UserAvrSocial(Base):
    __tablename__ = "user_data_avr_social"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    social_type: Mapped[int] = mapped_column(ForeignKey("CategorySocial.id"), nullable=True)
    value: Mapped[float]