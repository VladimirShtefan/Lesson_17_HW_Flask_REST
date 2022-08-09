from app.dao.base_dao import BaseDAO
from app.dao.models.directors import Director


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director

    def update_director(self, did: int, **kwargs) -> Director:
        director: Director = self.session.query(self.__model__).get_or_404(did)
        director.name = kwargs.get('name')
        self.session.add(director)
        self.session.commit()
        return director
