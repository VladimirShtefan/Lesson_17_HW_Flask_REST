from app.dao.base_dao import BaseDAO
from app.dao.models.genres import Genre


class GenreDAO(BaseDAO):
    def update_genre(self, mid: int, data: dict) -> Genre:
        genre: Genre = self.get_one_by_id(mid)
        genre.name = data.get('name')
        self.session.add(genre)
        self.session.commit()
        return genre
