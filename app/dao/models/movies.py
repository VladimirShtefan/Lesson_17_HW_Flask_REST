from app.app import db
from app.dao.models.directors import Director
from app.dao.models.genres import Genre


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
