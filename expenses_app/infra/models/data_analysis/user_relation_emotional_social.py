from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional
from ...database import Base

class UserRelationEmotionalSocial(Base):
    __tablename__ = "user_relation_emotional_social"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)
    social_type: Mapped[int] = mapped_column(ForeignKey("CategorySocial.id"), nullable=True)
    emotional_type: Mapped[int] = mapped_column(ForeignKey("CategoryEmotional.id"), nullable=True)
    value: Mapped[float]