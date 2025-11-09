import os
import csv

def ver_ganadores(archivo):
    """
        Verifica si existe el archivo y si esta muestra los puntajes
    """
    if not os.path.exists(archivo):
        print("No hay puntajes cargados")
        return
    else:
        with open(archivo,"r",encoding="utf-8") as file:
            leo = csv.reader(file)
            for x in leo:
                print(x)


def ingresa_ganador(archivo, total):
    """
        Pide la usuario su nombre y lo guarda junto a su puntaje obtenido
    """
    puntaje= {
                "nombre": input(f"Ingresa tu nombre:"),
                "high score": total
    }
    creado = os.path.exists(archivo)
    if creado:
        modo = "a"
    else:
        modo = "w"
    with open(archivo, modo, encoding="utf-8") as file:
        if not creado:
            file.write("NOMBRE,HIGH SCORE\n")
        file.write(f"{puntaje['nombre']},{puntaje['high score']}\n")