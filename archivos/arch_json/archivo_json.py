import os
import json

def guaradar_json(archivo):
    """
        Crea y guarda un archivo json con los valores de las jugadas y los simbolos de la tematica establecida.
    """
    configuracion = {
        "jugadas": {
            "escalera": 20,
            "full": 30,
            "poker": 40,
            "generala": 50,
        },
        "tematica": {
            "1": "Bulbasaur",
            "2": "Charmander",
            "3": "Squirtle",
            "4": "Pikachu",
            "5": "Nidoking",
            "6": "Blaziken"
        }
    }

    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(configuracion, file, indent=4)


def cargar_json(archivo):
    """
        Verifica si existe el archivo recibido como parametro. Si esta lo abre y lo guarda como un diccionario que luego retorna.
    """
    if not os.path.exists(archivo):
        return
    with open(archivo, "r", encoding= "utf-8") as file:
        diccionario = json.load(file)
    return diccionario
    