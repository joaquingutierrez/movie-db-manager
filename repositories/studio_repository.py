from .base import BaseRepository

class StudioRepository(BaseRepository):
    def __init__(self, db_path):
        super().__init__(db_path)
        sql = '''CREATE TABLE IF NOT EXISTS studios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL
                )'''
        self._cursor.execute(sql)
        self._conn.commit()

    def add(self, studio):
        sql = '''INSERT INTO studios (
        name, address) VALUES (
        ?, ?)'''
        parameters = (studio.name, studio.address)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def delete(self, studio_id):
        sql = "DELETE FROM studios WHERE id = ?"
        parameters = (studio_id,)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def update(self, studio_id, name=None, address=None):
        sql = "UPDATE studios SET "
        fields = []
        values = []

        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if address is not None:
            fields.append("address = ?")
            values.append(address)

        if not fields:
            raise ValueError("No fields provided to update.")

        sql += ", ".join(fields) + " WHERE id = ?"
        values.append(studio_id)

        self._cursor.execute(sql, tuple(values))
        self._conn.commit()

    def getAll(self):
        sql = "SELECT * FROM studios"
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def getById(self, studio_id):
        sql = "SELECT * FROM studios WHERE id = ?"
        parameters = (studio_id,)
        self._cursor.execute(sql, parameters)
        return self._cursor.fetchone()