def escalera(lista):
    lista.sort()
    total = 0
    for x in lista:
        if lista.index(x) == x - 1:
            total += 1
    if total == 5:
        return 20
    return 0
            

def full(lista):
    conjunto_dados = set(lista)
    total = 0
    for i in conjunto_dados:
        if lista.count(i) == 3 or lista.count(i) == 2:
            total += 1
        else:
            total -= 1
    if total == 2:
        return 30
    return 0

def poker(lista):
    conjunto_dados = set(lista)
    for x in conjunto_dados:
        if lista.count(x) == 4:
            return 40       
    return 0

def generala(lista):
    conjunto_dados = set(lista)
    for x in conjunto_dados:
        if lista.count(x) == 5:
            return 50
    return 0

def caras(lista):
    conjunto_dados = set(lista)
    for x in conjunto_dados:
        puntaje = lista.count(x) * x
    return puntaje
