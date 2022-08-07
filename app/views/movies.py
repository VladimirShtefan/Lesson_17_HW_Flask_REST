from flask_restx import Resource, Namespace

from app.api.api_models.movies import movie_model
from app.api.parsers import movie_filter, movie_model
from app.dao.base_dao import BaseDAO
from app.dao.models.movies import Movie
from app.dao.movie_dao import MovieDAO

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @movies_ns.expect(movie_filter)
    @movies_ns.marshal_list_with(movie_model, code=200)
    def get(self):
        """
        Get all movies
        """
        return BaseDAO(Movie).get_all()

    @movies_ns.expect(movie_model)
    @movies_ns.response(code=201, description='Created')
    @movies_ns.response(code=400, description='Bad request')
    @movies_ns.response(code=409, description='Record already exists')
    def post(self):
        """
        Create movie
        """
        data = movie_model.parse_args()
        MovieDAO(Movie).add_new_movie(data)
        # TODO: Тут нужно вернуть либо созданную запись либо ссылку на нее, точно не None
        return None, 201


@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    @movies_ns.marshal_with(movie_model, code=200, envelope='movie')
    def get(self, mid: int):
        """
        Get movie by id
        """
        return BaseDAO(Movie).get_one_by_id(mid)

    @movies_ns.expect(movie_model)
    @movies_ns.marshal_with(movie_model, code=200, envelope='movies', description='Updated')
    def put(self, mid: int):
        """
        Update movie
        """
        data = movie_model.parse_args()
        result = MovieDAO(Movie).update_movie(mid, data)
        return result

    @movies_ns.response(code=204, description='Deleted')
    def delete(self, mid):
        """
        Delete movie
        """
        MovieDAO(Movie).delete_movie(mid)
        return None, 204
