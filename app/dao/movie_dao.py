from app.dao.base_dao import BaseDAO
from app.dao.models.movies import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie
