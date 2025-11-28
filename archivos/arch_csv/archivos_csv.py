import os
from validaciones.validaciones import validar_iniciales_o_vacio

def cargar_estadisticas(archivo):
    """
        Verifica si existe el archivo, si esta guarda y devuelve una lista de diccionarios con los valores del archivo
    """
    estadisticas = []
    if not os.path.exists(archivo):
        return estadisticas
    
    with open(archivo,"r",encoding="utf-8") as file:
        file.readline()
        for x in file:
            elementos = x.split(",")
            jugador = {
                "nombre": elementos[0].strip(),
                "high score": elementos[1].strip()
            }
            estadisticas.append(jugador)
    return estadisticas


def ver_estadisticas(archivo):
    """
        Verifica si existe algun puntaje, luego imprime los 10 mayores puntajes.
    """
    puntajes = cargar_estadisticas(archivo)

    if puntajes == []:
        print("\nNo existen puntajes guardados")
    else:
        for j in range(len(puntajes) - 1):
            for x in range(len(puntajes) - j - 1):
                if int(puntajes[x]["high score"]) < int(puntajes[x + 1]["high score"]):
                    puntajes[x], puntajes[x + 1] = puntajes[x + 1], puntajes[x]
        print("\n" + "="*40)
        print(f"{'':>5}""NOMBRE" + f"{'-':^13}" + "HIGH SCORE")
        print("="*40)
        for i, puntos in enumerate(puntajes):
            if i == 9:
                print(f"{'':>6}"f"{puntos["nombre"]}" + f"{'=':^18}" + f"{puntos["high score"]:>3}")
                break
            print(f"{'':>6}"f"{puntos["nombre"]}" + f"{'=':^18}" + f"{puntos["high score"]:>3}")
            if i < len(puntajes) - 1:
                print("-"*40)
        print("="*40)


def ingresa_ganador(archivo, total):
    """
        Pide al usuario su nombre y lo guarda junto a su puntaje obtenido
    """
    nombre = input(f"\nIngresa iniciales (Tienen que ser 3): ").strip()
    while True:
        validar = validar_iniciales_o_vacio(nombre)
        if validar:
            break
        nombre = input(f"\nIngresa iniciales (Tienen que ser 3): ").strip()
    
    puntaje_final= {
                    "nombre": nombre.upper(),
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
        file.write(f"{puntaje_final['nombre']},{puntaje_final['high score']}\n")


def py_ingresa_ganador(archivo, total, nombre):
    """
        ingresa el nombre y el puntaje en un archivo csv
    """
    puntaje_final= {
                    "nombre": nombre.upper(),
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
        file.write(f"{puntaje_final['nombre']},{puntaje_final['high score']}\n")