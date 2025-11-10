import json

def guaradar_json(archivo):
    configuracion = {
        "jugadas": {
            "escalera": 20,
            "full": 30,
            "poker": 40,
            "generala": 50,
        },
        "tematica": {
            1: "Simbolo 1",
            2: "Simbolo 2",
            3: "Simbolo 3",
            4: "Simbolo 4",
            5: "Simbolo 5",
            6: "Simbolo 6",
        }
    }

    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(configuracion, file, indent=4)


def cargar_json():
    pass