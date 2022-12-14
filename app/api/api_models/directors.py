from flask_restx import fields

from app.app import api


director_model = api.model(
    'Director',
    {
        'pk': fields.Integer(attribute='id', required=True),
        'name': fields.String(required=True, max_length=255),
    }
)
