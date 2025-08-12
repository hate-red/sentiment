from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import joinedload

from app.database import async_session_maker
from app.service.base import BaseService
from app.history.models import History


class HistoryService(BaseService):
    model = History

    @classmethod
    async def get_history(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.user)) \
                                   .filter_by(user_id=user_id)
            result = await session.execute(query)
            records = result.scalars().all()
        
        if records:
            return records

        return {'detail': 'History not found'}
