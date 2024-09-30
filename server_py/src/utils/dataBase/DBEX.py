from fastapi import APIRouter, HTTPException, Request, status
from sqlmodel.ext.asyncio.session import AsyncSession
from config.db import Data, DataNoCommit


class DBEX:
    def controller_init(routerThis, description, DoService, Do, DoCreate) -> str:
        @routerThis.post(
            "/default_add",
            status_code=status.HTTP_201_CREATED,
            summary=f"添加{description}返回id",
        )
        async def add(do: DoCreate) -> str:
            return await DoService.add(do)

    # service初始化
    def service_init(DoService, DoDao, Do, DoCreate):
        # @classmethod
        @staticmethod
        async def add(do: DoCreate) -> str:
            return await DoDao.add(do)
        DoService.add = add

    def dao_init(DoDao, Do, DoCreate):

        @DataNoCommit
        async def add(do: DoCreate, session=AsyncSession) -> str:
            """插入一个新的do  无需显式调用 session.commit()，因为装饰器已经处理了"""
            db_do = Do.model_validate(do)
            session.add(db_do)
            await session.commit()
            return db_do.id
        DoDao.add = add
