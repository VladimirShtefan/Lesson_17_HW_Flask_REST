from app.dao.base_dao import BaseDAO
from app.dao.models.movies import Movie


class MovieDAO(BaseDAO):
    def get_movies_by_director_id(self, data: dict) -> list[Movie]:
        director_id = data.get('director_id')
        print(director_id)
        return self.session.query(self.model).filter(Movie.director_id == director_id).all()
