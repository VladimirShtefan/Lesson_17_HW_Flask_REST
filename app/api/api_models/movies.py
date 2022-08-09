from flask_restx import fields

from app.api.api_models.directors import director_model
from app.api.api_models.genres import genre_model
from app.app import api


movie_model = api.model(
    'Movie',
    {
        'id': fields.Integer(required=True),
        'title': fields.String(required=True, max_length=255),
        'description': fields.String(max_length=255),
        'trailer': fields.String(max_length=255),
        'year': fields.Integer(min=0),
        'rating': fields.Float(min=0.0, max=10.0),
        'genre_id': fields.Integer(required=True),
        'director_id': fields.Integer(required=True),
        'genre': fields.Nested(genre_model),
        'director': fields.Nested(director_model),
    }
)
