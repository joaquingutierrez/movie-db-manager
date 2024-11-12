from .base import IdClass

class StarsIn(IdClass):
    def __init__(self, movie_id, star_id):
        self.movie_id = self._validateId(movie_id)
        self.star_id = self._validateId(star_id)