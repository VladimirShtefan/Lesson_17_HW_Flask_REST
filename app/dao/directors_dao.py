from app.dao.base_dao import BaseDAO
from app.dao.models.directors import Director


class DirectorDAO(BaseDAO):
    def update_director(self, mid: int, data: dict) -> Director:
        director: Director = self.get_one_by_id(mid)
        director.name = data.get('name')
        self.session.add(director)
        self.session.commit()
        return director
