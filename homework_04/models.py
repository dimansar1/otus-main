"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, declared_attr
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
    Text,
)

class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

Base = declarative_base(cls=Base)

class User(Base):

    name = Column(String(32), nullable=False, unique=False)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String(120), nullable=True, unique=True)
    
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

class Post(Base):
    title = Column(
        String(120),
        nullable=False,
        unique=False,
    )
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:2602@localhost:5432/postgres"
DB_ECHO = False

async_engine = create_async_engine(
    url = PG_CONN_URI,
    echo = DB_ECHO
)

Session = sessionmaker(
    bind = async_engine,
    class_ = AsyncSession,
    expire_on_commit = False,
    autoflush = False, 
    autocommit = False,
)

