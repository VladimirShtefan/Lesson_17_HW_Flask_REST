from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.exc import IntegrityError

from app.constants import DATA_BASE_PATH
from data_base.fixtures.data import DATA

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATA_BASE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


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
        print('База уже создана')


if __name__ == '__main__':
    create_data()
