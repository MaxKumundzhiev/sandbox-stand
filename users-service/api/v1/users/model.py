from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from core.users_database.base_model import Base


class Users(Base):
    nickname: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)