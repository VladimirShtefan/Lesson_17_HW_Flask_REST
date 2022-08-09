from typing import TypeVar, List, Generic

from app.setup_db import db

T = TypeVar('T', bound=db.Model)


class BaseDAO(Generic[T]):
    __model__ = db.Model

    def __init__(self):
        self.session = db.session

    def get_all(self, **kwargs) -> List[T]:
        director_id = kwargs.get('director_id')
        genre_id = kwargs.get('genre_id')
        movie_query = self.session.query(self.__model__)
        if director_id:
            movie_query = movie_query.filter(self.__model__.director_id == director_id)
        if genre_id:
            movie_query = movie_query.filter(self.__model__.genre_id == genre_id)
        return movie_query.all()

    def get_one_by_id(self, id: int) -> T:
        return self.session.query(self.__model__).get_or_404(id)

    def delete_row(self, id: int):
        movie = self.session.query(self.__model__).get_or_404(id)
        self.session.delete(movie)
        self.session.commit()

    def add_row(self, **kwargs) -> T:
        new_row = self.__model__(**kwargs)
        with self.session.begin():
            self.session.add(new_row)
        return new_row

    def update_row(self, id: int, **kwargs) -> None:
        self.session.query(self.__model__).filter_by(id=id).update(kwargs)
        self.session.commit()
