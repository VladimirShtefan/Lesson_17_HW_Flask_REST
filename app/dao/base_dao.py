from typing import TypeVar, List, Generic
from abc import ABCMeta


from app.setup_db import db

T = TypeVar('T', bound=ABCMeta)


class BaseDAO(Generic[T]):
    __model__ = ABCMeta

    def __init__(self):
        self.session = db.session

    def get_all(self) -> List[T]:
        return self.session.query(self.__model__).all()

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
