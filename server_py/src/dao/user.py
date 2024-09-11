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
        await session.refresh(user)  # 刷新数据
        # 显示刷新  数据锁和同步问题
        return user.id

    @Data
    async def delete(id: str, session=AsyncSession):
        hero = await session.get(User, id)
        return await session.delete(hero)

    @Data
    async def update(user: User, session=AsyncSession):
        """更新用户信息"""
        user_to_upadte:User = await session.get(User, user.id)
        user_to_upadte.name = user.name
        user_to_upadte.email = user.email
        session.add(user_to_upadte)
        await session.commit()  # 提交事务
        session.refresh(user_to_upadte)
        return user_to_upadte

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
