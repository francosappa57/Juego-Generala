def validar_jugadas(jugadas, codigo):
    if jugadas[codigo] != 0 or jugadas[codigo] == "-":
        return False
    return True


def validar_puntaje(eleccion, puntajes_guardados, jugadas):
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
    for i in range(len(generala) - 1):
        for j in range(len(generala) - i - 1):
            if generala[j] != generala[j + 1]:
                return False
    return True

def validacion_guardado(valor):
        for x in valor.split(","):
            #print (valor[x])
            if x == "1" or x == "2" or x == "3" or x == "4" or x == "5":
                return True
            else:
                return False
            
#            if valor[x] not in "1" and valor[x] not in "2" and valor[x] not in "3" and valor[x] not in "4" and valor[x] != "5":
#                print(f"Solo se pueden ingresar valores del {rango1} al {rango2} separados por una coma.")
#                #valor = input(mensaje).strip()
#            else:
#                #print("testo")
#                return valor
            



