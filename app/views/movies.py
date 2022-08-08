from flask_restx import Resource, Namespace

from app.api.api_models.movies import movie_model
from app.api.parsers import movie_filter_parser, movie_model_parser
from app.dao.models.movies import Movie
from app.dao.base_dao import BaseDAO
from app.dao.movie_dao import MovieDAO


movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.expect(movie_filter_parser)
    @movies_ns.marshal_list_with(movie_model, code=200)
    def get(self):
        """
        Get all movies
        """
        data = movie_filter_parser.parse_args()
        result = MovieDAO(Movie).filter_movies(data)
        if result:
            return result, 200
        return BaseDAO(Movie).get_all(), 200

    @movies_ns.expect(movie_model_parser)
    @movies_ns.marshal_list_with(movie_model, code=201, description='Created')
    @movies_ns.response(code=400, description='Bad request')
    @movies_ns.response(code=409, description='Record already exists')
    def post(self):
        """
        Create movie
        """
        data = movie_model_parser.parse_args()
        return BaseDAO(Movie).add_row(data), 201


@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    @movies_ns.marshal_with(movie_model, code=200)
    def get(self, mid: int):
        """
        Get movie by id
        """
        return BaseDAO(Movie).get_one_by_id(mid), 200

    @movies_ns.expect(movie_model_parser)
    @movies_ns.marshal_with(movie_model, code=200, description='Updated')
    def put(self, mid: int):
        """
        Update movie
        """
        data = movie_model_parser.parse_args()
        return MovieDAO(Movie).update_movie(mid, data), 200

    @movies_ns.response(code=204, description='Deleted')
    def delete(self, mid: int):
        """
        Delete movie
        """
        BaseDAO(Movie).delete_row(mid)
        return None, 204
