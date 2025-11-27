import os
import json

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

archivo_juego_json = "archivos/arch_json/config.json"

def guaradar_json(archivo):
    """
        Crea y guarda un archivo json con los valores de las jugadas y los simbolos de la tematica establecida.
    """
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(configuracion, file, indent=4)


def cargar_json():
    """
        Verifica si existe el archivo recibido como parametro. Si esta lo abre y lo guarda como un diccionario que luego retorna.
    """
    if not os.path.exists(archivo_juego_json):
        guaradar_json(archivo_juego_json)
        return configuracion
    
    if os.path.exists(archivo_juego_json) != configuracion:
        guaradar_json(archivo_juego_json)
        return configuracion
   
    with open(archivo_juego_json, "r", encoding= "utf-8") as file:
        diccionario = json.load(file)
    
    if "config" not in diccionario:
        guaradar_json(archivo_juego_json)
        return configuracion
    
    return diccionario
    