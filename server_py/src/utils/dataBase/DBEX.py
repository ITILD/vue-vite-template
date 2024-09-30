from fastapi import APIRouter, HTTPException, Request, status
from sqlmodel.ext.asyncio.session import AsyncSession
from config.db import Data, DataNoCommit


class DBEX:
    def controller_init(routerThis, description, DoService, Do, DoCreate) -> str:
        @routerThis.post(
            "/default",
            status_code=status.HTTP_201_CREATED,
            summary=f"添加{description}返回id",
        )
        async def add(do: DoCreate) -> str:
            return await DoService.add(do)

        @routerThis.delete(
            "/default",
            summary=f"删除{description}",
        )
        async def delete(id: str):
            return await DoService.delete(id)

        @routerThis.put(
            "/default",
            summary=f"更新{description}",
        )
        async def update(do: Do):
            await DoService.update(do)

        @routerThis.get(
            "/default",
            status_code=status.HTTP_201_CREATED,
            summary=f"获取单个{description}",
        )
        async def select(id: str) -> Do | None:
            return await DoService.select(id)

        @routerThis.get(
            "/default/list",
            status_code=status.HTTP_201_CREATED,
            summary=f"获取批量{description}",
        )
        async def list():
            return await DoService.list()

    # service初始化
    def service_init(DoService, DoDao, Do, DoCreate):
        @staticmethod
        async def add(do: DoCreate) -> str:
            return await DoDao.add(do)
        DoService.add = add
        
        
        @staticmethod
        async def delete(id: str):
            await DoDao.delete(id)
        DoService.delete = delete

        @staticmethod
        async def update(do: Do):
            await DoDao.update(do)
        DoService.update = update
            
        @staticmethod
        async def select(id: str) -> Do | None:
            return await DoDao.select(id)
        DoService.select = select
        
        @staticmethod
        async def list():
            return await DoDao.list()
        DoService.list = list


    def dao_init(DoDao, Do, DoCreate):

        @DataNoCommit
        async def add(do: DoCreate, session=AsyncSession) -> str:
            """插入一个新的do  无需显式调用 session.commit()，因为装饰器已经处理了"""
            db_do = Do.model_validate(do)
            session.add(db_do)
            await session.commit()
            return db_do.id

        DoDao.add = add
