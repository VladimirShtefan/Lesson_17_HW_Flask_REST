from flask_restx import Resource, Namespace

from app.api.api_models.movies import movie_model
from app.api.parsers import director_parser, genre_parser, movie_parser
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
        return BaseDAO(Movie).get_all()

    @movies_ns.expect(movie_parser)
    @movies_ns.response(code=201, description='Created')
    @movies_ns.response(code=400, description='Bad request')
    @movies_ns.response(code=409, description='Record already exists')
    def post(self):
        data = movie_parser.parse_args()
        MovieDAO(Movie).add_new_movie(data)
        return None, 201


@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    @movies_ns.marshal_with(movie_model, code=200, envelope='movie')
    def get(self, mid):
        """
        get movie by id
        :param mid:
        :return:
        """
        return BaseDAO(Movie).get_one_by_id(mid)

    @movies_ns.expect(movie_parser)
    @movies_ns.marshal_with(movie_model, code=204, envelope='movies', description='Updated')
    def put(self, mid):
        data = movie_parser.parse_args()
        result = MovieDAO(Movie).update_movie(mid, data)
        return result

    @movies_ns.response(code=204, description='Deleted')
    def delete(self, mid):
        MovieDAO(Movie).delete_movie(mid)
        return None, 204


@movies_ns.route('/<int:director_id>/')
class MovieByDirectorView(Resource):
    @movies_ns.expect(director_parser)
    @movies_ns.marshal_list_with(movie_model, code=200, envelope='test')
    def get(self):
        data = director_parser.parse_args()
        return MovieDAO(Movie).get_movies_by_director_id(data['director_id']).all()
