import os

def cargar_estadisticas(archivo):
    """
        Verifica si existe el archivo y si esta muestra los puntajes
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
    puntajes = cargar_estadisticas(archivo)

    if puntajes == []:
        print("\nNo existen puntajes guardados")
    else:
        print("\n" + "="*40)
        print(f"{'':>5}""NOMBRE" + f"{'-':^13}" + "HIGH SCORE")
        print("="*40)
        for i, puntos in enumerate(puntajes):
            print(f"{'':>5}"f"{puntos["nombre"].title()}" + f"{'=':^13}" + f"{puntos["high score"]:>5}")
            if i < len(puntajes) - 1:
                print("-"*40)
        print("="*40)


def ingresa_ganador(archivo, total):
    """
        Pide la usuario su nombre y lo guarda junto a su puntaje obtenido
    """
    nombre = input(f"\nIngresa tu nombre: ")
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