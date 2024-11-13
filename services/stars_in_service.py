from .base import BaseService

class StarsInService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)
    
    def add(self, stars_in):
        try:
            self._repository.add(stars_in)
            print("Protagonización agregado con éxito")
        except ValueError as e:
            print("Error al agregar la Protagonización: ", e)
    
    def delete(self, movie_id, star_id):
        try:
            self._repository.delete(movie_id, star_id)
            print("Protagonización eliminada con éxito")
        except ValueError as e:
            print("Error al eliminar la Protagonización: ", e)
    
    def getAll(self):
        try:
            return self._repository.getAll()
        except ValueError as e:
            print("Error al leer las Protagonizaciones: ", e)