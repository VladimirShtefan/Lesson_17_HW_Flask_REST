from app.dao.base_dao import BaseDAO
from app.dao.models.movies import Movie
from flask_sqlalchemy import BaseQuery


class MovieDAO(BaseDAO):
    def get_movies_by_director_id(self, director_id: int) -> BaseQuery:
        return self.session.query(self.model).filter(Movie.director_id == director_id)

    def get_movies_by_genre_id(self, genre_id: int) -> BaseQuery:
        return self.session.query(self.model).filter(Movie.genre_id == genre_id)

    def add_new_movie(self, data) -> None:
        new_movie = Movie(**data)
        with self.session.begin():
            self.session.add(new_movie)

    def update_movie(self, mid, data) -> Movie:
        movie = self.get_one_by_id(mid)
        movie.director_id = data.get('director_id')
        movie.genre_id = data.get('genre_id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.rating = data.get('rating')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_movie(self, mid):
        movie = self.get_one_by_id(mid)
        self.session.delete(movie)
        self.session.commit()
