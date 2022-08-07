from app.constants import DATA_BASE_PATH


class Config:
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {
        'ensure_ascii': False,
    }


class DevConfig(Config):
    ENV = 'development'
    TEMPLATES_AUTO_RELOAD = 1
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATA_BASE_PATH}'


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
