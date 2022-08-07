import os

from flask import Flask

from app.config import DevConfig, ProdConfig
from app.setup_db import db

app = Flask(__name__)

if os.environ.get('FLASK_DEBUG') == '1':
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)

db.init_app(app)
