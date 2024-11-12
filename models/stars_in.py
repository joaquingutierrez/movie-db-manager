from .base import IdClass

class StarsIn(IdClass):
    def __init__(self, id, movie_id, star_id):
        super().__init__(id)
        self._movie_id = self._validateId(movie_id)
        self._star_id = self._validateId(star_id)