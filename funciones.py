import random

def jugar():
    guardados = []

    print("\nPLANTILLA")
    for turnos in range(3):
        print(f"\nTurno {turnos + 1}")
        jugada = tirada(guardados)
        if turnos == 2:
            pass
        else:
            valor_dados = guardar_dados(jugada)    
            for i in valor_dados:
                guardados.append(i)
        print(guardados)

def tirada(lista):
    lista_dados = []
    dados = 5
    inicio_caras = 1
    fin_caras = 6
    # if len(lista) == 0:
    for _ in range(dados - len(lista)):
        valor = random.randint(inicio_caras, fin_caras)
        lista_dados.append(valor)
    # else:
    #     for _ in range(dados - len(lista)):
    #         valor = random.randint(inicio_caras, fin_caras)
    #         lista_dados.append(valor)
    print(lista_dados)
    return lista_dados    


def guardar_dados(lista):
    dados_guardados = []
    
    pedido = input("Elige la posicion de los dados a guardar: ").split(',')

    if pedido == "":
        pass
    else:
        for i in range(len(lista)):
            for x in pedido:
                if int(x) == i:
                    dados_guardados.append(lista[i])
    return dados_guardados