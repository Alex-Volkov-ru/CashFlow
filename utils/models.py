from utils.database import Base
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    psw: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}, email={self.email!r}, psw={self.psw!r} )"

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column()
    category: Mapped[str] = mapped_column(String)
    decription: Mapped[str] = mapped_column(String(150))
    is_income: Mapped[bool] = mapped_column()
    date: Mapped[str] = mapped_column(String)


