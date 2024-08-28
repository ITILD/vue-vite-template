from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

# self
from config.db import Data,DataNoCommit
from do.user import User


class UserDao:

    @DataNoCommit
    async def add(user: User, session=AsyncSession) -> str:
        """插入一个新的用户  无需显式调用 session.commit()，因为装饰器已经处理了"""
        session.add(user)
        await session.commit()  # 提交事务
        await session.refresh(user)  # 提交事务
        # 显示刷新  数据锁和同步问题
        return user.id

    @Data
    async def delete(id: str, session=AsyncSession):
        return await session.delete(User, id)

    @Data
    async def update(name: str, email: str, session=AsyncSession):
        return await session.get(User, email)

    @DataNoCommit
    async def select(id: str, session=AsyncSession) -> User | None:
        return await session.get(User, id)

    @DataNoCommit
    async def list(session=AsyncSession) -> list[User]:
        result = await session.exec(select(User))
        users = result.all()
        return users

        # 快捷方式 id
        # sql = select(User).where(User.id == id)
        # print(sql) # 这里可以打印出sql
        # result = await session.execute(sql)
        # data = result.scalars().first()
