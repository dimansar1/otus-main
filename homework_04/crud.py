
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, Post

async def create_users(session: AsyncSession, users_data: list) -> None:
    users = [
        User(
            id=el['id'],
            name=el['name'],
            username=el['username'],
            email=el['email'],
        )
        for el in users_data
    ]
    session.add_all(users)
    await session.commit()

async def create_posts(session: AsyncSession, posts_data: list) -> None:
    posts = [
        Post(
            id=el['id'],
            title=el['title'],
            body=el['body'],
            user_id=el['userId'],
        )
        for el in posts_data
    ]
    session.add_all(posts)
    await session.commit()
