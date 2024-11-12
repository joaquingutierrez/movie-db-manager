from .base import IdClass

class Movie(IdClass):
    def __init__(self, id, title, year, duration, studio_id):
        super().__init__(id)
        self._title = self._validateTitle(title)
        self._year = self._validateYear(year)
        self._duration = self._validateDuration(duration)
        self._studio_id = self._validateId(studio_id)

    def _validateTitle(self, title):
        title = str(title).strip()
        if len(title) > 50:
            raise ValueError("Title must be 50 characters or fewer.")
        return title
    
    def _validateYear(self, year):
        try:
            year = int(year)
        except ValueError:
            raise ValueError("Year must be an integer.")
        if 1400 <= year <= 2030:
            return year
        raise ValueError("Year must be between 1400 and 2030.")
    
    def _validateDuration(self, duration):
        try:
            duration = int(duration)
        except ValueError:
            raise ValueError("Duration must be an integer.")
        if 1 <= duration <= 500:
            return duration
        raise ValueError("Duration must be between 1 and 500.")
    
        
    def __str__(self):
        return  f"Título: {self._title} \n" \
                f"Año: {self._year}\n" \
                f"Duración: {self._duration}\n" \
                f"Id del Estudio: {self._studio_id}"