from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from app.config import get_db_url


DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Shortcuts for type annotations in database models
int_pk = Annotated[int, mapped_column(primary_key=True)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]

# additional columns for each table in database
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=func.now())]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
