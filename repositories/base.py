class BaseRepository:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = conn.cursor()
    
    def add(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def getAll(self):
        pass

    def getById(self):
        pass