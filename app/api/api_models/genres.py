from flask_restx import fields

from app.app import api


genre_model = api.model(
    'Genre',
    {
        'pk': fields.Integer(attribute='id', required=True),
        'name': fields.String(required=True, max_length=255),
    }
)
