from flask_restx import Resource, Namespace

from app.api.api_models.movies import movie_model
from app.api.parsers import movie_filter_parser, movie_model_parser
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
        return MovieDAO().get_all(**data), 200

    @movies_ns.expect(movie_model_parser)
    @movies_ns.marshal_list_with(movie_model, code=201, description='Created')
    @movies_ns.response(code=400, description='Bad request')
    @movies_ns.response(code=409, description='Record already exists')
    def post(self):
        """
        Create movie
        """
        data = movie_model_parser.parse_args()
        return MovieDAO().add_row(**data), 201


@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    @movies_ns.marshal_with(movie_model, code=200)
    def get(self, mid: int):
        """
        Get movie by id
        """
        return MovieDAO().get_one_by_id(mid), 200

    @movies_ns.expect(movie_model_parser)
    @movies_ns.response(code=204, description='Updated')
    def put(self, mid: int):
        """
        Update movie
        """
        data = movie_model_parser.parse_args()
        return MovieDAO().update_row(mid, **data), 204

    @movies_ns.response(code=204, description='Deleted')
    def delete(self, mid: int):
        """
        Delete movie
        """
        MovieDAO().delete_row(mid)
        return None, 204
