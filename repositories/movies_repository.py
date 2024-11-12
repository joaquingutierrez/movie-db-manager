from .base import BaseRepository

class MovieRepository(BaseRepository):
    def __init__(self, db_path):
        super().__init__(db_path)
        sql = '''CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    year INTEGER NOT NULL CHECK(year BETWEEN 1400 AND 2030),
                    duration INTEGER NOT NULL CHECK(duration BETWEEN 1 AND 500),
                    studio_id INTEGER NOT NULL,
                    FOREIGN KEY (studio_id) REFERENCES studio(id)
                )'''
        self._cursor.execute(sql)
        self._conn.commit()

    def add(self, movie):
        sql = '''INSERT INTO movies (
        title, year, duration, studio_id) VALUES (
        ?, ?, ?, ?)'''
        parameters = (movie.title, movie.year, movie.duration, movie.studio_id)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def delete(self, movie_id):
        sql = '''DELETE FROM movies WHERE id = ?;'''
        parameters = (movie_id,)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def update(self, movie_id, title=None, year=None, duration=None, studio_id=None):
        sql = "UPDATE movies SET "
        fields = []
        values = []

        if title is not None:
            fields.append("title = ?")
            values.append(title)
        if year is not None:
            fields.append("year = ?")
            values.append(year)
        if duration is not None:
            fields.append("duration = ?")
            values.append(duration)
        if studio_id is not None:
            fields.append("studio_id = ?")
            values.append(studio_id)

        if not fields:
            raise ValueError("No fields provided to update.")

        sql += ", ".join(fields) + " WHERE id = ?"
        values.append(movie_id)

        self._cursor.execute(sql, tuple(values))
        self._conn.commit()

    def getAll(self):
        sql = "SELECT * FROM movies"
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def getById(self, movie_id):
        sql = "SELECT * FROM movies WHERE id = ?"
        parameters = (movie_id)
        self._cursor.execute(sql, parameters)
        return self._cursor.fetchall()