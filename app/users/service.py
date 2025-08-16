from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.service.base import BaseService
from app.users.models import User


class UserService(BaseService):
    model = User


    @classmethod
    async def get_user(cls, user_id: int):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(joinedload(cls.model.history))
                .filter_by(id=user_id)
            )
            result = await session.execute(query)
            user = result.unique().scalar_one_or_none()

        return user
    

    @classmethod
    async def get_users(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.history)) \
                                     .filter_by(**filter_by)
            result = await session.execute(query)
            users = result.unique().scalars().all()

        return users
