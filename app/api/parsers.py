from flask_restx.reqparse import RequestParser


movie_filter_parser: RequestParser = RequestParser()
movie_filter_parser.add_argument('director_id', type=int, location='args')
movie_filter_parser.add_argument('genre_id', type=int, location='args')

movie_model_parser: RequestParser = RequestParser()
movie_model_parser.add_argument('title', location='json', type=str, required=True, nullable=False)
movie_model_parser.add_argument('description', location='json', type=str, required=False, nullable=True)
movie_model_parser.add_argument('trailer', location='json', type=str, required=False, nullable=True)
movie_model_parser.add_argument('year', location='json', type=int, required=False, nullable=True)
movie_model_parser.add_argument('rating', location='json', type=float, required=False, nullable=True)
movie_model_parser.add_argument('genre_id', location='json', type=int, required=True, nullable=False)
movie_model_parser.add_argument('director_id', location='json', type=int, required=True, nullable=False)

name_model_parser: RequestParser = RequestParser()
name_model_parser.add_argument('name', location='json', type=str, required=True, nullable=False)
