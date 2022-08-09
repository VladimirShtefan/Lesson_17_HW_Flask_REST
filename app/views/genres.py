from flask_restx import Resource, Namespace

from app.api.api_models.genres import genre_model
from app.api.parsers import name_model_parser
from app.dao.genres_dao import GenreDAO

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @genre_ns.marshal_list_with(genre_model, code=200)
    def get(self):
        """
        Get all genres
        """
        return GenreDAO().get_all(), 200

    @genre_ns.expect(name_model_parser)
    @genre_ns.marshal_list_with(genre_model, code=201, description='Created')
    @genre_ns.response(code=400, description='Bad request')
    @genre_ns.response(code=409, description='Record already exists')
    def post(self):
        """
        Create genre
        """
        data = name_model_parser.parse_args()
        return GenreDAO().add_row(**data), 201


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    @genre_ns.marshal_with(genre_model, code=200)
    def get(self, gid: int):
        """
        Get genre by id
        """
        return GenreDAO().get_one_by_id(gid), 200

    @genre_ns.expect(name_model_parser)
    @genre_ns.response(code=204, description='Updated')
    def put(self, gid: int):
        """
        Update genre
        """
        data = name_model_parser.parse_args()
        return GenreDAO().update_row(gid, **data), 204

    @genre_ns.response(code=204, description='Deleted')
    def delete(self, gid: int):
        """
        Delete genre
        """
        GenreDAO().delete_row(gid)
        return None, 204
