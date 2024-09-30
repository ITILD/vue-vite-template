# # self
# # from config.log import console
# from config.fastapi_config import app
# from service.dict import DictService
# from do.dict import Dict, DictCreate
# from utils.dataBase.DBEX import DBEX

# # lib
# from fastapi.responses import JSONResponse
# from fastapi import APIRouter, HTTPException, Request, status

# router = APIRouter()

# DBEX.controller_init(router, "dict", DictService,Dict, DictCreate)

# app.include_router(router, prefix="/dict", tags=["字典"])

