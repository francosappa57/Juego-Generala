def escalera(lista):
    lista.sort()
    primera_escalera = [1,2,3,4,5]
    segunda_escalera = [2,3,4,5,6]
    
    if lista == primera_escalera:
        return 20
    elif lista == segunda_escalera:
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
    numeros = {"uno": 0,
               "dos": 0,
               "tres": 0,
               "cuatro": 0,
               "cinco": 0,
               "seis": 0,}
    conjunto_dados = set(lista)
    
    for x in conjunto_dados:
        total = lista.count(x) * x
        if x == 1:
            numeros["uno"] = total
        elif x == 2:
            numeros["dos"] = total
        elif x == 3:
            numeros["tres"] = total
        elif x == 4:
            numeros["cuatro"] = total
        elif x == 5:
            numeros["cinco"] = total
        elif x == 6:
            numeros["seis"] = total
    return numeros
