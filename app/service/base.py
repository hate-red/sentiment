from sqlalchemy import select

from app.database import async_session_maker


class BaseService:
    model = None


    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            instances = result.scalars().all()

        if instances:
            return instances

        return {'detail': 'Not found'}

    @classmethod
    async def get_one_or_none_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            instance = result.scalar_one_or_none()
        
        if instance:
            return instance
        
        return {'detail': 'Not found'}
