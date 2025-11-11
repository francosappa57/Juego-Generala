import validaciones.validaciones as val
from archivos.arch_json.constantes import JUGADAS

def escalera(lista, categorias, verificar):
    """
        Calcula si los valores obtenidos dan Escalera
    """

    codigo = "escalera"
    lista.sort()
    primera_escalera = (1,2,3,4,5)
    segunda_escalera = (2,3,4,5,6)
    
    if val.validar_jugadas(verificar, codigo):
        if lista == primera_escalera:
            categorias['7'] = JUGADAS[codigo]
        elif lista == segunda_escalera:
            categorias['7'] = JUGADAS[codigo]
        return
    categorias['7'] = "-"
    return
            

def full(lista, categorias, verificar):
    """
        Calcula si los valores obtenidos dan Full
    """
    codigo = "full"
    conjunto_dados = set(lista)
    total = 0
    if val.validar_jugadas(verificar, codigo):
        for i in conjunto_dados:
            if lista.count(i) == 3 or lista.count(i) == 2:
                total += 1
            else:
                total -= 1
        if total == 2:
            categorias['8'] = JUGADAS[codigo]
        return
    categorias['8'] = "-"
    return


def poker(lista, categorias, verificar):
    """
        Calcula si los valores ingresados dan Poker
    """
    codigo = "poker"
    conjunto_dados = set(lista)
    if val.validar_jugadas(verificar, codigo):
        for x in conjunto_dados:
            if lista.count(x) == 4:
                categorias['9'] = JUGADAS[codigo]
        return
    categorias['9'] = "-"
    return


def generala(categorias, verificar,lista=None):
    """
        Calcula si los valores ingresados dan Generala
    """
    if lista == None:
        primero = val.validacion_generala_servida(categorias)
        if primero:
            return primero
        return
    codigo = "generala"
    conjunto_dados = set(lista)
    if val.validar_jugadas(verificar, codigo):
        for x in conjunto_dados:
            if lista.count(x) == 5:
                categorias['10'] = JUGADAS[codigo]
        return
    categorias['10'] = "-"
    return


def caras(lista, categorias, verificar):
    """
        Calcula los valores obtenidos de las caras y suma los repetidos
    """
    for i, j in enumerate(verificar):
        if i + 1 < 7:
            if val.validar_jugadas(verificar, j):
                total = lista.count(i + 1) * (i + 1)
                categorias[str(i + 1)] = total
            else:
                categorias[str(i + 1)] = "-"
    return
    

def calcular_total(puntajes):
    """
        Calcula el total de puntajes obtenidos de las jugadas
    """
    total = 0
    for suma in puntajes.values():
        if suma != "-":
            total += suma
    return total
