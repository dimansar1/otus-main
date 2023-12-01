from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String

from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query
    

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    if TYPE_CHECKING:
        query: Query