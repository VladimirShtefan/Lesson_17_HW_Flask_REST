from flask_restx.reqparse import RequestParser


director_parser: RequestParser = RequestParser()
director_parser.add_argument(name='director_id', type=int, location='args', required=False)
