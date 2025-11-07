def validar_jugadas(jugadas, codigo):
    if jugadas[codigo] != 0:
        return False
    return True


def validar_puntaje(eleccion, puntajes_guardados, jugadas):
    for i, j in enumerate(puntajes_guardados):
        if i + 1 == int(eleccion):
            if jugadas[eleccion] != 0 and jugadas[eleccion] != '-':
                puntajes_guardados[j] = jugadas[eleccion]
                return True
            print("\nJugada no disponible. Ingrese otra opcion...")
            return False
    print("\nOpcion Invalida")
    return False
