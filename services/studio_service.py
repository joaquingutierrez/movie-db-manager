from .base import BaseService

class StudioService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)
    
    def add(self, studio):
        try:
            self._repository.add(studio)
            print("Estudio agregado con éxito")
        except ValueError as e:
            print("Error al agregar el Estudio: ", e)
    
    def update(self, studio_id, name=None, address=None):
        try:
            self._repository.update(studio_id, name, address)
            print("Estudio actualizado con éxito")
        except ValueError as e:
            print("Error al actualizar el Estudio: ", e)
    
    def delete(self, studio_id):
        try:
            self._repository.delete(studio_id)
            print("Estudio eliminado con éxito")
        except ValueError as e:
            print("Error al eliminar el Estudio: ", e)
    
    def getAll(self):
        try:
            return self._repository.getAll()
        except ValueError as e:
            print("Error al leer los Estudios: ", e)
    
    def getById(self, studio_id):
        try:
            return self._repository.getById(studio_id)
        except ValueError as e:
            print("Error al leer los Estudios: ", e)