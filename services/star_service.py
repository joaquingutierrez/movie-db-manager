from .base import BaseService

class StarService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)
    
    def add(self, star):
        try:
            self._repository.add(star)
            print("Estrella agregada con éxito")
        except ValueError as e:
            print("Error al agregar la Estrella: ", e)
    
    def update(self, star_id, name=None, address=None, gender=None, birth_date=None):
        try:
            self._repository.update(star_id, name, address, gender, birth_date)
            print("Estrella actualizada con éxito")
        except ValueError as e:
            print("Error al actualizar la Estrella: ", e)
    
    def delete(self, star_id):
        try:
            self._repository.delete(star_id)
            print("Estrella eliminada con éxito")
        except ValueError as e:
            print("Error al eliminar la Estrella: ", e)
    
    def getAll(self):
        try:
            return self._repository.getAll()
        except ValueError as e:
            print("Error al leer las Estrellas: ", e)
    
    def getById(self, studio_id):
        try:
            return self._repository.getById(studio_id)
        except ValueError as e:
            print("Error al leer las Estrellas: ", e)