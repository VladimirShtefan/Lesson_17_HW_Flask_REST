from flask_restx import fields

from app.app import api


genre_model = api.model(
    'Genre',
    {
        'pk': fields.Integer(attribute='id'),
        'name': fields.String(),
    }
)
