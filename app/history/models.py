from sqlalchemy import ForeignKey, Text, text, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, str_uniq, int_pk


class History(Base):
    __tablename__ = 'history'

    id: Mapped[int_pk]
    content: Mapped[str] = mapped_column(Text)
    avg_sentiment: Mapped[float]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    
    user: Mapped['User'] = relationship('User', back_populates='history')

    def __str__(self):
        return f'{self.content :20}... Average sentiment: {self.avg_sentiment}'

    
    def __repr__(self):
        return str(self)


    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'avg_sentiment': self.avg_sentiment,
            'user_id': self.user_id
        }
