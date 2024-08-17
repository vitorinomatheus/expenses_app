from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] 
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]