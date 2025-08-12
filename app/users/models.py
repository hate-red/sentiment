from sqlalchemy import ForeignKey, Text, text, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, str_uniq, int_pk


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int_pk]
    username: Mapped[str_uniq]
    email: Mapped[str_uniq]
    role: Mapped[str]

    history: Mapped[list['History']] = relationship('History', back_populates='user')


    def __str__(self):
        return f'{self.username}: {self.role}'


    def __repr__(self):
        return str(self)
