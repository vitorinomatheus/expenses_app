from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from typing import Optional

class CategoriesBase:
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    custom: Mapped[bool]
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("CategoryBudgetImpact.id"), nullable=True)
