from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional

class UserRelationEmotionalSocial:
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    social_type: Mapped[int] = mapped_column(ForeignKey("CategorySocial.id"), nullable=True)
    emotional_type: Mapped[int] = mapped_column(ForeignKey("CategoryEmotional.id"), nullable=True)
    value: Mapped[float]