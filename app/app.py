import os
from typing import Type

from flask import Flask

from app.config import DevConfig, ProdConfig, Config
from app.setup_api import api
from app.setup_db import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movies_ns


def create_app() -> Flask:
    application: Flask = Flask(__name__)
    match os.environ.get('FLASK_ENV'):
        case 'development':
            config_app(application, DevConfig)
        case 'production':
            config_app(application, ProdConfig)
        case _:
            raise RuntimeError('Need to set environment variable FLASK_ENV')
    db.init_app(application)
    api.init_app(application)
    api.add_namespace(movies_ns, '/api/movies')
    api.add_namespace(genre_ns, '/api/genres')
    api.add_namespace(director_ns, '/api/directors')
    return application


def config_app(application: Flask, config: Type[Config]) -> None:
    application.config.from_object(config)
    application.app_context().push()
