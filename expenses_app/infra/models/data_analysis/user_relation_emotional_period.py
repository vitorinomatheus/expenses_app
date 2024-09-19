from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional

class UserRelationEmotionalPeriod:
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    month_week: Mapped[Optional[int]]
    emotional_type: Mapped[int] = mapped_column(ForeignKey("CategoryEmotional.id"), nullable=True)
    value: Mapped[float]