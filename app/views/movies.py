from flask_restx import Resource, Namespace

from app.api.api_models.movies import movie_model
from app.api.parsers import director_parser
from app.dao.models.movies import Movie
from app.dao.base_dao import BaseDAO
from app.dao.movie_dao import MovieDAO


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.marshal_list_with(movie_model, code=200, envelope='movies')
    def get(self):
        """
        get all movies
        :return:
        """
        all_movies = BaseDAO(Movie).get_all()
        return all_movies


@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    @movies_ns.marshal_with(movie_model, code=200, envelope='movie')
    def get(self, mid):
        """
        get movie by id
        :param mid:
        :return:
        """
        movie = BaseDAO(Movie).get_one_by_id(mid)
        return movie


@movies_ns.route('/<int:director_id>/')
class MovieByDirectorView(Resource):
    @movies_ns.expect(director_parser)
    @movies_ns.marshal_with(movie_model, code=200, envelope='movies_by_director_id')
    def get(self):
        """
        get movie by director_id
        :return:
        """
        data = director_parser.parse_args()
        movies = MovieDAO(Movie).get_movies_by_director_id(**data)
        return movies
