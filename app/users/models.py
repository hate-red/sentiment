from sqlalchemy import text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, str_uniq, int_pk


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int_pk]
    username: Mapped[str_uniq]
    email: Mapped[str_uniq]
    password: Mapped[str]

    # roles
    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_premium: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_super_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    history: Mapped[list['History']] = relationship('History', back_populates='user')


    def __str__(self):
        return f'id = {self.id :5}{self.username}'


    def __repr__(self):
        return str(self)
