from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.exc import IntegrityError

from app.constants import DATA_BASE_PATH_FOR_DEV
from test_data_base.fixtures.data import DATA

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATA_BASE_PATH_FOR_DEV}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)
    director = db.relationship("Director")

    __table_args__ = (
        db.CheckConstraint('year > 0'),
        db.CheckConstraint('rating >= 0 and rating <= 10')
    )


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


def create_data():
    db.create_all()
    for movie in DATA["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )
        db.session.add(m)

    for director in DATA["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"],
        )
        db.session.add(d)

    for genre in DATA["genres"]:
        d = Genre(
            id=genre["pk"],
            name=genre["name"],
        )
        db.session.add(d)
    try:
        db.session.commit()
    except IntegrityError:
        print('???????? ?????? ?????????????? ?????? ???????????????? ???? ???????????? ????????????, ?????????????????? ????????')


if __name__ == '__main__':
    create_data()
