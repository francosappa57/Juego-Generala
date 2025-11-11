import os
from validaciones.validaciones import no_blank

def cargar_estadisticas(archivo):
    """
        Verifica si existe el archivo, si esta guarda y devuelve un diccionario con los valores del archivo
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
            if i > 9:
                break
            print(f"{'':>5}"f"{puntos["nombre"].title()}" + f"{'=':^13}" + f"{puntos["high score"]:>5}")
            if i < len(puntajes) - 2:
                print("-"*40)
        print("="*40)


def ingresa_ganador(archivo, total):
    """
        Pide la usuario su nombre y lo guarda junto a su puntaje obtenido
    """
    while True:
        nombre = input(f"\nIngresa tu nombre: ")
        
        validar = no_blank(nombre)
        if validar:
            break
        print("No se permiten espacion en blanco")
    
    puntaje_final= {
                    "nombre": nombre,
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