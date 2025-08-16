from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError

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
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            instance = result.scalar_one_or_none()
        
        if instance:
            return instance
        
        return None


    @classmethod
    async def create(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)

                try:
                    await session.commit()
                
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

        return new_instance


    @classmethod
    async def update(cls, filter_by: dict, **values):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    update(cls.model)
                    .where(
                        *[getattr(cls.model, key) == value
                        for key, value in filter_by.items()]
                    )
                    .values(**values)
                    .execution_options(syncronize_session='fetch')
                )
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

        return result.rowcount


    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            async with session.begin():
                query = delete(cls.model).filter_by(**filter_by)
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

        return result.rowcount
