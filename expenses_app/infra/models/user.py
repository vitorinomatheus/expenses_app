from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] 
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]

    @classmethod
    def get_json_schema(cls) -> SQLAlchemyAutoSchema:
        return UserJsonSchema()

class UserJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationship = True
        load_instance = True