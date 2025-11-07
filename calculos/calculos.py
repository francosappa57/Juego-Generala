import validaciones.validaciones as val

def escalera(lista, categorias, verificar):
    codigo = "escalera"
    lista.sort()
    primera_escalera = [1,2,3,4,5]
    segunda_escalera = [2,3,4,5,6]
    
    if val.validar_jugadas(verificar, codigo):
        if lista == primera_escalera:
            categorias['7'] = 20
        elif lista == segunda_escalera:
            categorias['7'] = 20
        return
    categorias['7'] = "-"
    return
            

def full(lista, categorias, verificar):
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
            categorias['8'] = 30
        return
    categorias['8'] = "-"
    return


def poker(lista, categorias, verificar):
    codigo = "poker"
    conjunto_dados = set(lista)
    if val.validar_jugadas(verificar, codigo):
        for x in conjunto_dados:
            if lista.count(x) == 4:
                categorias['9'] = 40       
        return
    categorias['9'] = "-"
    return


def generala(categorias, verificar,lista=None):
    if lista == None:
        primera = val.validacion_generala_servida(categorias)
        if primera:
            return primera
        return
    codigo = "generala"
    conjunto_dados = set(lista)
    if val.validar_jugadas(verificar, codigo):
        for x in conjunto_dados:
            if lista.count(x) == 5:
                categorias['10'] = 50
        return
    categorias['10'] = "-"
    return


def caras(lista, categorias, verificar):
    for i, j in enumerate(verificar):
        if i + 1 < 7:
            if val.validar_jugadas(verificar, j):
                total = lista.count(i + 1) * (i + 1)
                categorias[str(i + 1)] = total
            else:
                categorias[str(i + 1)] = "-"
    return
    

def calcular_total(puntajes):
    total = 0
    for suma in puntajes.values():
        if suma != "-":
            total += suma
    return total
