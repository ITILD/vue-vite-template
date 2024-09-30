# from sqlmodel.ext.asyncio.session import AsyncSession
# from sqlmodel import select

# # self
# from config.db import Data,DataNoCommit
# from do.dict import Dict,DictCreate, DictPublic


# class DictDao:
#     @DataNoCommit
#     async def add(dict: DictCreate, session=AsyncSession) -> str:
#         """插入一个新的用户  无需显式调用 session.commit()，因为装饰器已经处理了"""
#         db_dict = Dict.model_validate(dict)
#         session.add(db_dict)
#         await session.commit()  # 提交事务
#         # await session.refresh(db_dict)  # 刷新数据
#         # 显示刷新  数据锁和同步问题
#         return db_dict.id

#     @Data
#     async def delete(id: str, session=AsyncSession):
#         hero = await session.get(Dict, id)
#         return await session.delete(hero)

#     @Data
#     async def update(dict: Dict, session=AsyncSession):
#         """更新用户信息"""
#         dict_to_upadte:Dict = await session.get(Dict, dict.id)
#         dict_to_upadte.name = dict.name
#         dict_to_upadte.email = dict.email
#         session.add(dict_to_upadte)
#         await session.commit()  # 提交事务
#         session.refresh(dict_to_upadte)
#         return dict_to_upadte

#     @DataNoCommit
#     async def select(id: str, session=AsyncSession) -> Dict | None:
#         return await session.get(Dict, id)

#     @DataNoCommit
#     async def list(session=AsyncSession) -> list[Dict]:
#         result = await session.exec(select(Dict))
#         dicts = result.all()
#         return dicts
