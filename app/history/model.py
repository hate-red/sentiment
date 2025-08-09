from sqlalchemy import ForeignKey, Text, text, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, str_uniq, int_pk, str_null_true
from app.users.model import User


class History(Base):
    id: Mapped[int_pk]
    content: Mapped[str] = mapped_column(Text, nullable=False)
    avg_sentiment: Mapped[float] = mapped_column(Numeric, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    user: Mapped['User'] =  relationship('User', back_populates='history')

    def __str__(self):
        return f'{self.content :20}, {self.avg_sentiment}'


    def __repr__(self):
        return str(self)
