from app.setup_db import db
from flask_sqlalchemy.model import DefaultMeta


class BaseDAO:
    def __init__(self, model):
        self.session = db.session
        self.model = model

    def get_all(self) -> list[DefaultMeta]:
        return self.session.query(self.model).all()

    def get_one_by_id(self, id: int):
        return self.session.query(self.model).get_or_404(id)

    def delete_row(self, mid: int):
        movie = self.get_one_by_id(mid)
        self.session.delete(movie)
        self.session.commit()

    def add_row(self, data: dict) -> DefaultMeta:
        new_row = self.model(**data)
        with self.session.begin():
            self.session.add(new_row)
        return new_row

