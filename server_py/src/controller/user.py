# self
# from config.log import console
from uuid import UUID, uuid4
from config.fastapi_config import app
from service.user import UsersService
from do.user import User

# lib
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException, Request, status

router = APIRouter()

# post
@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add(user: User):
    try:
        # 调用函数
        await UsersService.add(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


# get
@router.get("/select_by_id", status_code=status.HTTP_201_CREATED)
async def select_by_id(id: str) -> User | None:
    return await UsersService.select_by_id(id)


# update
@router.put("/update_by_email")
async def update_by_email(name: str, email: str):
    await UsersService.update_by_email(name, email)
    
# delete
@router.delete("/delete_by_id")
async def delete_by_id(id: str):
    await UsersService.delete_by_id(id)


app.include_router(router, prefix="/user", tags=["user"])
