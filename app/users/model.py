from sqlalchemy import ForeignKey, Text, text, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, str_uniq, int_pk, str_null_true


class User(Base):
    id: Mapped[int_pk]
    username: Mapped[str_uniq]
    email: Mapped[str_uniq]
    role: Mapped[str] = mapped_column(server_default='default')


    def __str__(self):
        return f'{self.username}, {self.role}'


    def __repr__(self):
        return str(self)