# self
# from config.log import console
from config.fastapi_config import app
from service.user import UsersService
from do.user import User, UserCreate

# lib
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException, Request, status

router = APIRouter()

controller_init(router, "user", UsersService,User, UserCreate)

@router.post("/", status_code=status.HTTP_201_CREATED, summary="添加用户返回id")
async def add(user: UserCreate) -> str:
    return await UsersService.add(user)


@router.delete("/")
async def delete(id: str):
    await UsersService.delete(id)


@router.put("/")
async def update(user: User):
    await UsersService.update(user)


@router.get("/", status_code=status.HTTP_201_CREATED)
async def select(id: str) -> User | None:
    return await UsersService.select(id)


@router.get("/list", status_code=status.HTTP_201_CREATED)
async def list() -> list[User]:
    return await UsersService.list()


app.include_router(router, prefix="/dict", tags=["字典"])

