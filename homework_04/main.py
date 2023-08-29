"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from models import async_engine, Session, User, Post, Base
from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL
from crud import create_users, create_posts

async def drop_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await async_engine.dispose()

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await async_engine.dispose()

async def set_dates():
    async with Session() as session:
        users_data: list[User]
        posts_data: list[Post]
        users_data, posts_data = await asyncio.gather(
            fetch_json(USERS_DATA_URL),
            fetch_json(POSTS_DATA_URL),
        )
        await create_users(session=session, users_data=users_data)
        await create_posts(session=session, posts_data=posts_data)

async def async_main():
    await drop_tables()
    await create_tables()
    await set_dates()

def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
