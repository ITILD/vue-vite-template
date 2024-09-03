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
class DBConnectType:
    sqlite = "sqlite+aiosqlite"
    postgresql = "postgresql+asyncpg"
    # mysql = "mysql+aiomysql://"


class SqlConnect:
    url: str = None
    pwd: str = None
    host: str = None
    port: int = None
    engine: create_async_engine = None

    def __init__(
        self, type: DBConnectType, path: str, user: str, pwd: str, host: str, port: int
    ):
        if type == DBConnectType.sqlite:
            self.url = f"{type}:///{path}"
        elif type == DBConnectType.postgresql:
            # postgresql+asyncpg://hero:heroPass123@0.0.0.0:5432/heroes_db
            self.url = f"{type}://{user}:{pwd}@{host}:{port}/{path}"
        # todo: mysql
        #  "mysql+pymysql://user:password@host:port/database"

    def connect(self, url: str):
        self.url = url


SQLALCHEMY_DATABASE_URL = "source/db/base.db"
SQL_TYPE_SQLITE = "sqlite+aiosqlite:///"
# 注意：需要提前安装pymysql， pip install pymysql
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@host:port/database"
# 数据库连接列表
SQL_LIST = [{"value": SQL_TYPE_SQLITE + SQLALCHEMY_DATABASE_URL, type: "sqlite"}]


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
