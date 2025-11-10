import validaciones.validaciones as val
import json

archivo_tematica = "archivos/tematica.json"

def escalera(lista, categorias, verificar):
    """
        Calcula si los valores obtenidos dan Escalera
    """
    with open(archivo_tematica) as archivo:
        diccionario_escalera= json.load(archivo)
    codigo = "escalera"
    lista.sort()
    primera_escalera = diccionario_escalera["jugadas"]["escalera"][0]["condicion1"]
    segunda_escalera = diccionario_escalera["jugadas"]["escalera"][0]["condicion2"]
    
    if val.validar_jugadas(verificar, codigo):
        if lista == primera_escalera:
            categorias['7'] = diccionario_escalera["jugadas"]["escalera"][0]["puntuacion"]
        elif lista == segunda_escalera:
            categorias['7'] = diccionario_escalera["jugadas"]["escalera"][0]["puntuacion"]
        return
    categorias['7'] = "-"
    return
            

def full(lista, categorias, verificar):
    """
        Calcula si los valores obtenidos dan Full
    """
    with open(archivo_tematica) as archivo:
        diccionario_full= json.load(archivo)
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
            categorias['8'] = diccionario_full["jugadas"]["full"][0]["puntuacion"]
        return
    categorias['8'] = "-"
    return


def poker(lista, categorias, verificar):
    """
        Calcula si los valores ingresados dan Poker
    """
    with open(archivo_tematica) as archivo:
        diccionario_poker= json.load(archivo)
    codigo = "poker"
    conjunto_dados = set(lista)
    if val.validar_jugadas(verificar, codigo):
        for x in conjunto_dados:
            if lista.count(x) == 4:
                categorias['9'] = diccionario_poker["jugadas"]["poker"][0]["puntuacion"]  
        return
    categorias['9'] = "-"
    return


def generala(categorias, verificar,lista=None):
    """
        Calcula si los valores ingresados dan Generala
    """
    with open(archivo_tematica) as archivo:
        diccionario_generala= json.load(archivo)
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
                categorias['10'] = diccionario_generala["jugadas"]["generala"][0]["puntuacion"] 
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
