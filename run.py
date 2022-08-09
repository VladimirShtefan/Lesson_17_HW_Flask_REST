import os

from app.app import create_app

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
