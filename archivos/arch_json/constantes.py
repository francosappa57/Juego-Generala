import os
from archivos.arch_json.archivo_json import guaradar_json, cargar_json


archivo_juego_json = "config.json"
guaradar_json(archivo_juego_json)
variable = cargar_json(archivo_juego_json)


EMBLEMAS = variable["tematica"]
JUGADAS = variable["jugadas"]