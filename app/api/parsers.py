from flask_restx.reqparse import RequestParser


director_parser: RequestParser = RequestParser()
director_parser.add_argument('director_id', type=int, location='args')

genre_parser: RequestParser = RequestParser()
genre_parser.add_argument('genre_id', type=int, location='args')

movie_parser: RequestParser = RequestParser()
movie_parser.add_argument('title', location='form', type=str, required=True, nullable=False)
movie_parser.add_argument('description', location='form', type=str, required=False, nullable=True)
movie_parser.add_argument('trailer', location='form', type=str, required=False, nullable=True)
movie_parser.add_argument('year', location='form', type=int, required=False, nullable=True)
movie_parser.add_argument('rating', location='form', type=float, required=False, nullable=True)
movie_parser.add_argument('genre_id', location='form', type=int, required=True, nullable=False)
movie_parser.add_argument('director_id', location='form', type=int, required=True, nullable=False)
