class IdClass:
    def __init__(self, id):
        self._id = self._validateId(id)

    def _validateId (self, id):
        try:
            id = int(id)
        except ValueError:
            raise ValueError("Id must be an integer.")
        if id >= 1:
            return id
        else:
            raise ValueError("Id must be above zero.")