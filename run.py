import os

from app.app import app


if __name__ == '__main__':
    os.environ['FLASK_DEBUG'] = '1'
    app.run(host='0.0.0.0', port=5000)