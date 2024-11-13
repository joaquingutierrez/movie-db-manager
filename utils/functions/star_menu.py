from models.star import Star
from utils.const.db import star_service

def starMenu():
    print("-----Menu de Estrellas-----")
    op = 0
    while op != 9:
        print("1. Crear Estrella")
        print("2. Modificar Estrella")
        print("3. Eliminar Estrella")
        print("4. Lista de Estrellas")
        print("9. Volver al Menú principal")

        try:
            op = int(input("Ingrese la opción deseada: "))
        except Exception:
            print("Opción no válida.")

        if op == 1:
            print("CREAR")
            addStar()
        if op == 2:
            print("MODIFICAR")
            updateStar()
        if op == 3:
            print("ELIMINAR")
            deleteStar()
        if op == 4:
            print("Lista")
            getAllStars()
        if op == 9:
            print("-----Volviendo-----")

def addStar():
    while True:
        name = input("Ingrese el nombre completo: ")
        address = input("Ingrese la dirección: ")
        gender = input("Ingrese el género (M/F): ")
        birth_date = input("Ingrese la fecha de nacimiento: ")
        try:
            new_star = Star(name, address, gender, birth_date)
            star_service.add(new_star)
            break
        except ValueError as e:
            print("No se pudo crear la Estrella: ", e)

def updateStar():
    while True:
        star_id = input("Ingrese el ID de la Estrella a Modificar: ")
        name = input("Ingrese el nuevo nombre: ")
        address = input("Ingrese la nueva Dirección: ")
        gender = input("Ingrese el género (M/F): ")
        birth_date = input("Ingrese la fecha de nacimiento: ")
        try:
            new_star = Star(name, address, gender, birth_date)
            star_id = int(star_id)
            star_service.update(star_id, name, address, gender, birth_date)
            break
        except ValueError as e:
            print("Error: ", e)

def deleteStar():
    while True:
        star_id = input("Ingrese el ID de la Estrella a Eliminar: ")
        try:
            star_id = int(star_id)
            star_service.delete(star_id)
            break
        except ValueError as e:
            print("No se pudo borrar la Estrella: ", e)

def getAllStars():
    try:
        stars = star_service.getAll()
        for star in stars:
            print("id: ",star[0])
            print("Nombre: ", star[1])
            print("Dirección: ", star[2])
            print("Género: ", star[3])
            print("Fecha de nacimiento: ", star[4])
            print("")
    except ValueError as e:
        print("Error: ", e)