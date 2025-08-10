from sqlalchemy import select

from app.database import async_session_maker
from app.service.base import BaseService
from app.users.model import User


class UserService(BaseService):
    model = User
