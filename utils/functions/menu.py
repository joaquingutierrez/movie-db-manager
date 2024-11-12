from .studio_menu import studioMenu
from .movie_menu import movieMenu

def menu():
    print("-----Menu Principal-----")
    op = 0
    while op != 9:
        print("1. Menu de Peliculas")
        print("2. Menu de Estrellas")
        print("3. Menu de Estudios")
        print("4. Menu de Protagonizadas")
        print("9. Terminar")
        try:
            op = int(input("Ingrese la opción deseada: "))
        except Exception as e:
            print("Opción no válida.")
    
        if op == 1:
            print("-----Menu de Peliculas-----")
            movieMenu()
        if op == 2:
            print("-----Menu de Estrellas-----")
        if op == 3:
            studioMenu()
        if op == 4:
            print("-----Menu de Protagonizadas-----")
        if op == 9:
            print("-----Fin del Programa-----")