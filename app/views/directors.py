from flask_restx import Resource, Namespace

from app.api.api_models.directors import director_model
from app.api.parsers import name_model_parser
from app.dao.base_dao import BaseDAO
from app.dao.directors_dao import DirectorDAO
from app.dao.models.directors import Director


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @director_ns.marshal_list_with(director_model, code=200)
    def get(self):
        """
        Get all directors
        """
        return BaseDAO(Director).get_all(), 200

    @director_ns.expect(name_model_parser)
    @director_ns.marshal_list_with(director_model, code=201, description='Created')
    @director_ns.response(code=400, description='Bad request')
    @director_ns.response(code=409, description='Record already exists')
    def post(self):
        """
        Create director
        """
        data = name_model_parser.parse_args()
        return BaseDAO(Director).add_row(data), 201


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    @director_ns.marshal_with(director_model, code=200)
    def get(self, did: int):
        """
        Get director by id
        """
        return BaseDAO(Director).get_one_by_id(did), 200

    @director_ns.expect(name_model_parser)
    @director_ns.marshal_with(director_model, code=200, description='Updated')
    def put(self, did: int):
        """
        Update director
        """
        data = name_model_parser.parse_args()
        return DirectorDAO(Director).update_director(did, data), 200

    @director_ns.response(code=204, description='Deleted')
    def delete(self, did: int):
        """
        Delete director
        """
        BaseDAO(Director).delete_row(did)
        return None, 204
