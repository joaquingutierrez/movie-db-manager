from .base import BaseRepository

class StarRepository(BaseRepository):
    def __init__(self, db_path):
        super().__init__(db_path)
        sql = '''CREATE TABLE IF NOT EXISTS stars (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    gender TEXT CHECK(gender IN ('M', 'F', 'O')) NOT NULL,
                    birth_date DATE NOT NULL
                )'''
        self._cursor.execute(sql)
        self._conn.commit()

    def add(self, star):
        sql = '''INSERT INTO stars (
        name, address, gender, birth_date) VALUES (
        ?, ?, ?, ?)'''
        parameters = (star.name, star.address, star.gender, star.birth_date)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def delete(self, star_id):
        sql = "DELETE FROM stars WHERE id = ?"
        parameters = (star_id,)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def update(self, star_id, name=None, address=None, gender=None, birth_date=None):
        sql = "UPDATE stars SET "
        fields = []
        values = []

        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if address is not None:
            fields.append("address = ?")
            values.append(address)
        if gender is not None:
            fields.append("gender = ?")
            values.append(gender)
        if birth_date is not None:
            fields.append("birth_date = ?")
            values.append(birth_date)

        if not fields:
            raise ValueError("No fields provided to update.")

        sql += ", ".join(fields) + " WHERE id = ?"
        values.append(star_id)

        self._cursor.execute(sql, tuple(values))
        self._conn.commit()

    def getAll(self):
        sql = "SELECT * FROM stars"
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def getById(self, star_id):
        sql = "SELECT * FROM stars WHERE id = ?"
        parameters = (star_id,)
        self._cursor.execute(sql, parameters)
        return self._cursor.fetchall()