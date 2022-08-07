import os

from flask import Flask

from app.config import DevConfig, ProdConfig
from app.setup_api import api
from app.setup_db import db
from app.views.movies import movies_ns

app = Flask(__name__)

if os.environ.get('FLASK_ENV', 'development'):
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)

db.init_app(app)
api.init_app(app)


api.add_namespace(movies_ns, '/api/movies')
