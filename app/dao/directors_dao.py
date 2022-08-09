from app.dao.base_dao import BaseDAO
from app.dao.models.directors import Director


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director
