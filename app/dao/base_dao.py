from app.setup_db import db


class BaseDAO:
    def __init__(self, model):
        self.session = db.session
        self.model = model

    def get_all(self):
        return self.session.query(self.model).all()

    def get_one_by_id(self, id: int):
        return self.session.query(self.model).get_or_404(id)


