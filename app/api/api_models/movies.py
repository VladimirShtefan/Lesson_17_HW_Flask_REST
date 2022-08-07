from flask_restx import fields

from app.api.api_models.directors import director_model
from app.api.api_models.genres import genre_model
from app.app import api


movie_model = api.model(
    'Movie',
    {
        'id': fields.Integer(),
        'title': fields.String(),
        'description': fields.String(),
        'trailer': fields.String(),
        'year': fields.Integer(),
        'rating': fields.Float(),
        'genre_id': fields.Integer(),
        'director_id': fields.Integer(),
        'genre': fields.Nested(genre_model),
        'director': fields.Nested(director_model),
    }
)
