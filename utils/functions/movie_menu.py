from models.movie import Movie
from utils.const.db import movie_service

def movieMenu():
    print("-----Menu de Peliculas-----")
    op = 0
    while op != 9:
        print("1. Crear Pelicula")
        print("2. Modificar Pelicula")
        print("3. Eliminar Pelicula")
        print("4. Lista de Peliculas")
        print("9. Volver al Menú principal")

        try:
            op = int(input("Ingrese la opción deseada: "))
        except Exception:
            print("Opción no válida.")

        if op == 1:
            print("CREAR")
            add()
        if op == 2:
            print("MODIFICAR")
            update()
        if op == 3:
            print("ELIMINAR")
            delete()
        if op == 4:
            print("Lista")
            getAll()
        if op == 9:
            print("-----Volviendo-----")

def add():
    while True:
        title = input("Ingrese el título: ")
        year = input("Ingrese el año: ")
        duration = input("Ingrese la duracion en min: ")
        studio_id = input("Ingrese el ID del Estudio: ")
        try:
            new_movie = Movie(title, year, duration, studio_id)
            movie_service.add(new_movie)
            break
        except ValueError as e:
            print("No se pudo crear la Pelicula: ", e)

def update():
    while True:
        movie_id = input("Ingrese el ID de la Pelicula a Modificar: ")
        title = input("Ingrese el título: ")
        year = input("Ingrese el año: ")
        duration = input("Ingrese la duracion en min: ")
        studio_id = input("Ingrese el ID del Estudio: ")
        try:
            new_movie = Movie(title, year, duration, studio_id)
            movie_id = int(movie_id)
            movie_service.update(movie_id, title, year, duration, studio_id)
            break
        except ValueError as e:
            print("Error: ", e)

def delete():
    while True:
        movie_id = input("Ingrese el ID de la Pelicula que desea Borrar: ")
        try:
            movie_id = int(movie_id)
            movie_service.delete(movie_id)
            break
        except ValueError as e:
            print("No se pudo borrar la Pelicula: ", e)

def getAll():
    try:
        movies = movie_service.getAll()
        for movie in movies:
            print("id: ",movie[0])
            print("Título: ", movie[1])
            print("Año: ", movie[2])
            print("Duración: ", movie[3])
            print("ID Del Estudio: ", movie[4])
            print("")
    except ValueError as e:
        print("Error: ", e)