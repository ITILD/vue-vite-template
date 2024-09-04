# self
from config.log import console

# lib
from functools import wraps

# from sqlalchemy import create_engine
# import aiosqlite # 依赖写全防止找不到
from sqlmodel import create_engine, Session
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker


# 枚举类
class DataLoaderType:
    sqlite = "sqlite+aiosqlite"
    postgresql = "postgresql+asyncpg"
    # mysql = "mysql+aiomysql://"


class DataLoaderInterface:

    def __init__(self):
        raise NotImplementedError

    def connect(self):
        raise NotImplementedError

class SqlConnect:
    url: str = None
    pwd: str = None
    host: str = None
    port: int = None
    engine: create_async_engine = None
    def __init__(
        self, type: DataLoaderType, path: str, user: str, pwd: str, host: str, port: int
    ):
        # 打包跟随程序
        if type == DataLoaderType.sqlite:
            self.url = f"{type}:///{path}"
        # 远程
        elif type == DataLoaderType.postgresql:
            # postgresql+asyncpg://hero:heroPass123@0.0.0.0:5432/heroes_db
            self.url = f"{type}://{user}:{pwd}@{host}:{port}/{path}"
        # todo: mysql
        #  "mysql+pymysql://user:password@host:port/database"
    def connect(self, url: str):
        self.engine = url


SQLALCHEMY_DATABASE_URL = "source/db/base.db"
SQL_TYPE_SQLITE = "sqlite+aiosqlite:///"



engine = create_async_engine(
    SQL_TYPE_SQLITE + SQLALCHEMY_DATABASE_URL,
    echo=True,  # 控制台打印SQL
)

sessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def Data(f):
    """装饰器_负责创建执行和关闭"""

    @wraps(f)
    async def wrapper(*args, **kwargs):
        try:
            # 创建一个配置过的Session类
            async with sessionLocal() as session:  # 确保 session 总是被关闭
                # 设置session类型
                kwargs["session"] = session  # 将 session 作为关键字参数传递给 f
                result = await f(*args, **kwargs)
                await session.commit()  # 提交事务
                return result
        except Exception as e:
            # console.exception("数据库问题:"+str(e.orig))
            console.error("数据库问题:" + str(e))
            raise e

    return wrapper


def DataNoCommit(f):
    """装饰器_负责创建执行和关闭"""

    @wraps(f)
    async def wrapper(*args, **kwargs):
        try:
            # 创建一个配置过的Session类
            async with sessionLocal() as session:  # 确保 session 总是被关闭
                # 设置session类型
                kwargs["session"] = session  # 将 session 作为关键字参数传递给 f
                result = await f(*args, **kwargs)
                return result
        except Exception as e:
            # console.exception("数据库问题:"+str(e.orig))
            console.error("数据库问题:" + str(e))
            raise e

    return wrapper


console.log("...数据库配置完成")
