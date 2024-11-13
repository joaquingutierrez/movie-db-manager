from .studio_menu import studioMenu
from .movie_menu import movieMenu
from .star_menu import starMenu
from .stars_in_menu import starsInMenu

def menu():
    print("-----Menu Principal-----")
    op = 0
    while op != 9:
        print("1. Menu de Peliculas")
        print("2. Menu de Estrellas")
        print("3. Menu de Estudios")
        print("4. Menu de Protagonizaciones")
        print("9. Terminar")
        try:
            op = int(input("Ingrese la opción deseada: "))
        except Exception as e:
            print("Opción no válida.")
    
        if op == 1:
            movieMenu()
        if op == 2:
            starMenu()
        if op == 3:
            studioMenu()
        if op == 4:
            starsInMenu()
        if op == 9:
            print("-----Fin del Programa-----")