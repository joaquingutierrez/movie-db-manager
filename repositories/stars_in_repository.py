from .base import BaseRepository

class StarsInRepository(BaseRepository):
    def __init__(self, db_path):
        super().__init__(db_path)
        sql = '''CREATE TABLE IF NOT EXISTS starsIn (
                    movie_id INTEGER NOT NULL,
                    star_id INTEGER NOT NULL,
                    FOREIGN KEY (movie_id) REFERENCES movies(id),
                    FOREIGN KEY (star_id) REFERENCES stars(id),
                    PRIMARY KEY (movie_id, star_id)
                );'''
        self._cursor.execute(sql)
        self._conn.commit()

    def add(self, stars_in):
        sql = '''INSERT INTO starsIn (
        movie_id, star_id) VALUES (
        ?, ?)'''
        parameters = (stars_in.movie_id, stars_in.star_id)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def delete(self, movie_id, star_id):
        sql = "DELETE FROM starsIn WHERE movie_id = ? and star_id = ?"
        parameters = (movie_id, star_id)
        self._cursor.execute(sql, parameters)
        self._conn.commit()

    def getAll(self):
        sql = "SELECT * FROM starsIn"
        self._cursor.execute(sql)
        return self._cursor.fetchall()