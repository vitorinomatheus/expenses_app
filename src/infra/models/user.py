from .. import database
from sqlalchemy.orm import Mapped, mapped_column

class User(database.Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] 
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]

    def __repr__(self) -> str:
        return f"Id: {self.id}; Email: {self.Email}"
