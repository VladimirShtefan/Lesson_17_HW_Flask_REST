from app.dao.base_dao import BaseDAO
from app.dao.models.movies import Movie


class MovieDAO(BaseDAO):
    def filter_movies(self, data: dict) -> list[Movie] | None:
        director_id = data.get('director_id')
        genre_id = data.get('genre_id')
        if not director_id and not genre_id:
            return None
        movie_query = self.session.query(self.model)
        if director_id:
            movie_query = movie_query.filter(Movie.director_id == director_id)
        if genre_id:
            movie_query = movie_query.filter(Movie.genre_id == genre_id)
        return movie_query.all()

    def update_movie(self, mid: int, data: dict) -> Movie:
        movie: Movie = self.get_one_by_id(mid)
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
