from app.dao.base_dao import BaseDAO
from app.dao.models.genres import Genre


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre
