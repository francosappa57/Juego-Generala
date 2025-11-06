def escalera(lista):
    conjunto_dados = set(lista)
    for x in conjunto_dados:
        if lista.count(x) == 1:
            total = 0
            total += x
            if total == 15 or total == 20:
                return 20
    return 0

def full(lista):
    conjunto_dados = set(lista)
    full = 0
    for i in conjunto_dados:
        if lista.count(i) == 3:
            full += 3
        else:
            full += 2
    if full == 5:
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
