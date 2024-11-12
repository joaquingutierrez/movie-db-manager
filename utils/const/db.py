import sqlite3

from repositories.studio_repository import StudioRepository
from repositories.movies_repository import MovieRepository

from services.studio_service import StudioService
from services.movie_service import MovieService

conn = sqlite3.connect("storage/movies.db")

studio_repo = StudioRepository(conn)
movie_repo = MovieRepository(conn)

studio_service = StudioService(studio_repo)
movie_service = MovieService(movie_repo)