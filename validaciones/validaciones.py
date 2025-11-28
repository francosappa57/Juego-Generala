def validar_jugadas(jugadas, codigo):
    """
         Valida si la jugada ya fue utilizada
    """
    if jugadas[codigo] != 0 or jugadas[codigo] == "-":
        return False
    return True


def validar_puntaje(eleccion, puntajes_guardados, jugadas):
    """
        Valida y verifica si es posible realizar la jugada seleccionada
    """
    for i, j in enumerate(puntajes_guardados):
        if i + 1 == int(eleccion):
            if jugadas[eleccion] != 0 and jugadas[eleccion] != '-':
                puntajes_guardados[j] = jugadas[eleccion]
                return True
            elif jugadas[eleccion] == 0:
                return j
            print("\nJugada no disponible. Ingrese otra opcion...")
            return False
    print("\nOpcion Invalida")
    return False


def validacion_generala_servida(generala):
    """
        Comprueba si el usuario obtiene generala en el primer turno y devuelve un valor booleano
    """
    for i in range(len(generala) - 1):
        for j in range(len(generala) - i - 1):
            if generala[j] != generala[j + 1]:
                return False
    return True

def validacion_guardado(valor):
    """
        Valida los valores ingresados de la funcion guardar_dados
    """
    for x in valor.split(","):
        if x == "1" or x == "2" or x == "3" or x == "4" or x == "5":
            return True
        else:
            return False
            
def validar_eleccion(valor, puntajes):
    """
        Valida los valores ingresados de la funcion posibles_jugadas
    """
    for x in puntajes.keys():
        if valor == x:
            return True
    return False


def validar_iniciales_o_vacio(nombre):
    if nombre == "":
        print("\nNo se permiten espacios en blanco")
        return False
    
    if len(nombre) != 3:
        print("\nSolo ingresar 3 iniciales")
        return False
    
    return True

            



