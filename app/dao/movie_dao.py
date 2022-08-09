from typing import List

from app.dao.base_dao import BaseDAO
from app.dao.models.movies import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def filter_movies(self, **kwargs) -> List[Movie]:
        director_id = kwargs.get('director_id')
        genre_id = kwargs.get('genre_id')
        movie_query = self.session.query(self.__model__)
        if director_id:
            movie_query = movie_query.filter(Movie.director_id == director_id)
        if genre_id:
            movie_query = movie_query.filter(Movie.genre_id == genre_id)
        return movie_query.all()

    def update_movie(self, mid: int, **kwargs) -> Movie:
        movie: Movie = self.session.query(self.__model__).get_or_404(mid)
        movie.director_id = kwargs.get('director_id')
        movie.genre_id = kwargs.get('genre_id')
        movie.title = kwargs.get('title')
        movie.description = kwargs.get('description')
        movie.rating = kwargs.get('rating')
        movie.trailer = kwargs.get('trailer')
        movie.year = kwargs.get('year')
        self.session.add(movie)
        self.session.commit()
        return movie
