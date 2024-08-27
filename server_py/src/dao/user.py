# self
from uuid import UUID, uuid4

from sqlmodel import select
from config.db import Data
from do.user import User
from sqlmodel.ext.asyncio.session import AsyncSession


class UserDao:

    @Data
    async def insert(user: User, session=AsyncSession):
        """插入一个新的用户"""
        r = session.add(user)
        return r
        # 不需要显式调用 session.commit()，因为装饰器已经处理了

    @Data
    async def select_by_id(id: str, session=AsyncSession) -> User|None:
        # 快捷方式 id
        # sql = select(User).where(User.id == id)
        # print(sql) # 这里可以打印出sql
        # result = await session.execute(sql)
        # data = result.scalars().first()
        user = await session.get(User, id)
        return user
