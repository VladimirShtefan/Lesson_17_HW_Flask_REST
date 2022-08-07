from flask_restx.reqparse import RequestParser

movie_filter: RequestParser = RequestParser()
movie_filter.add_argument('director_id', type=int, location='args')
movie_filter.add_argument('genre_id', type=int, location='args')

movie_model: RequestParser = RequestParser()
movie_model.add_argument('title', location='json', type=str, required=True, nullable=False)
movie_model.add_argument('description', location='json', type=str, required=False, nullable=True)
movie_model.add_argument('trailer', location='json', type=str, required=False, nullable=True)
movie_model.add_argument('year', location='json', type=int, required=False, nullable=True)
movie_model.add_argument('rating', location='json', type=float, required=False, nullable=True)
movie_model.add_argument('genre_id', location='json', type=int, required=True, nullable=False)
movie_model.add_argument('director_id', location='json', type=int, required=True, nullable=False)
