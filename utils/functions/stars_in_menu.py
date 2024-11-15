from models.stars_in import StarsIn
from utils.const.db import stars_in_service
from utils.const.db import movie_service
from utils.const.db import star_service

def starsInMenu():
    print("-----Menu de Protagonizaciones-----")
    op = 0
    while op != 9:
        print("1. Crear Protagonización")
        print("3. Eliminar Protagonización")
        print("4. Lista de Protagonizaciones")
        print("9. Volver al Menú principal")

        try:
            op = int(input("Ingrese la opción deseada: "))
        except Exception:
            print("Opción no válida.")

        if op == 1:
            print("CREAR")
            add()
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
        movie_id = input("Ingrese el ID de la Pelicula: ")
        star_id = input("Ingrese el ID de la Estrella: ")
        try:
            new_stars_in = StarsIn(movie_id, star_id)
            stars_in_service.add(new_stars_in)
            break
        except ValueError as e:
            print("No se pudo crear la Protagonización: ", e)

def delete():
    while True:
        print("Ingrese los IDs para eliminar...")
        movie_id = input("Ingrese el ID de la Pelicula: ")
        star_id = input("Ingrese el ID de la Estrella: ")
        try:
            new_stars_in = StarsIn(movie_id, star_id)
            stars_in_service.delete(movie_id, star_id)
            break
        except ValueError as e:
            print("No se pudo borrar la Protagonización: ", e)

def getAll():
    try:
        stars_in = stars_in_service.getAll()
        for item in stars_in:
            print("ID de la Pelicula: ", item[0])
            print("ID de la Estrella: ", item[1])
            movie = movie_service.getById(item[0])
            star = star_service.getById(item[1])
            if (movie is not None):
                print("Título de la Película: ", movie[1])
                print("Año de la Película: ", movie[2])
            else:
                print("Título de la Película: No encontrado")
                print("Año de la Película: No encontrado")

            if (star is not None):
                print("Nombre de la Estrella: ", star[1])
            else:
                print("Nombre de la Estrella: No encontrado")

            print("")
    except ValueError as e:
        print("Error: ", e)