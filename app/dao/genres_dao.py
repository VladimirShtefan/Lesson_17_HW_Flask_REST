from app.dao.base_dao import BaseDAO
from app.dao.models.genres import Genre


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre

    def update_genre(self, gid: int, **kwargs) -> Genre:
        genre: Genre = self.session.query(self.__model__).get_or_404(gid)
        genre.name = kwargs.get('name')
        self.session.add(genre)
        self.session.commit()
        return genre
