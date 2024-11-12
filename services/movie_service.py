from .base import BaseService

class MovieService(BaseService):
    def __init__(self, repository):
        super().__init__(repository)
    
    def add(self, movie):
        try:
            self._repository.add(movie)
            print("Pelicula agregada con éxito")
        except ValueError as e:
            print("Error al agregar la Pelicula: ", e)
    
    def update(self, movie_id, title=None, year=None, duration=None, studio_id=None):
        try:
            self._repository.update(movie_id, title, year, duration, studio_id)
            print("Pelicula actualizada con éxito")
        except ValueError as e:
            print("Error al actualizar la Pelicula: ", e)
    
    def delete(self, movie_id):
        try:
            self._repository.delete(movie_id)
            print("Pelicula eliminada con éxito")
        except ValueError as e:
            print("Error al eliminar la Pelicula: ", e)
    
    def getAll(self):
        try:
            return self._repository.getAll()
        except ValueError as e:
            print("Error al leer las Peliculas: ", e)
    
    def getById(self, studio_id):
        try:
            return self._repository.getById(studio_id)
        except ValueError as e:
            print("Error al leer las Peliculas: ", e)