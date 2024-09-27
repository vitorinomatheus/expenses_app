from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional
from ...database import Base

class UserRelationSocialPeriod(Base):
    __tablename__ = "user_relation_social_period"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    event_type: Mapped[int] = mapped_column(ForeignKey("CategorySocial.id"), nullable=True)
    month_week: Mapped[Optional[int]]
    value: Mapped[float]