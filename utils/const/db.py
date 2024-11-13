import sqlite3

from repositories.studio_repository import StudioRepository
from repositories.movies_repository import MovieRepository
from repositories.star_repository import StarRepository
from repositories.stars_in_repository import StarsInRepository

from services.studio_service import StudioService
from services.movie_service import MovieService
from services.star_service import StarService
from services.stars_in_service import StarsInService

conn = sqlite3.connect("storage/movies.db")

studio_repo = StudioRepository(conn)
movie_repo = MovieRepository(conn)
star_repo = StarRepository(conn)
stars_in_repo = StarsInRepository(conn)

studio_service = StudioService(studio_repo)
movie_service = MovieService(movie_repo)
star_service = StarService(star_repo)
stars_in_service = StarsInService(stars_in_repo)