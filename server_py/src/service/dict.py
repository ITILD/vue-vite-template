# self
from do.dict import Dict,DictCreate
from dao.dict import DictDao
from utils.dataBase.DBEX import DBExtention
# lib


class DictService:
    """dict"""

DBExtention.service_init(DictService,DictDao,Dict,DictCreate)