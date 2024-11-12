from models.studio import Studio
from utils.const.db import studio_service

def studioMenu():
    print("-----Menu de Estudios-----")
    op = 0
    while op != 9:
        print("1. Crear Estudio")
        print("2. Modificar Estudio")
        print("3. Eliminar Estudio")
        print("4. Lista de Estudios")
        print("9. Volver al Menú principal")

        try:
            op = int(input("Ingrese la opción deseada: "))
        except Exception:
            print("Opción no válida.")

        if op == 1:
            print("CREAR")
            addStudio()
        if op == 2:
            print("MODIFICAR")
            updateStudio()
        if op == 3:
            print("ELIMINAR")
            deleteStudio()
        if op == 4:
            print("Lista")
            getAllStudios()
        if op == 9:
            print("-----Volviendo-----")

def addStudio():
    while True:
        name = input("Ingrese el nombre del Estudio: ")
        address = input("Ingrese la dirección del Estudio: ")
        try:
            new_studio = Studio(name, address)
            studio_service.add(new_studio)
            break
        except ValueError as e:
            print("No se pudo crear el estudio: ", e)

def updateStudio():
    while True:
        studio_id = input("Ingrese el ID del Estudio a Modificar: ")
        name = input("Ingrese el nuevo nombre: ")
        address = input("Ingrese la nueva Dirección: ")
        try:
            new_studio = Studio(name, address)
            studio_id = int(studio_id)
            studio_service.update(studio_id, name, address)
            break
        except ValueError as e:
            print("Error: ", e)

def deleteStudio():
    while True:
        studio_id = input("Ingrese el ID del Estudio a Modificar: ")
        try:
            studio_id = int(studio_id)
            studio_service.delete(studio_id)
            break
        except ValueError as e:
            print("No se pudo borrar el estudio: ", e)

def getAllStudios():
    try:
        studios = studio_service.getAll()
        for studio in studios:
            print("id: ",studio[0])
            print("Nombre: ", studio[1])
            print("Dirección: ", studio[2])
            print("")
    except ValueError as e:
        print("Error: ", e)