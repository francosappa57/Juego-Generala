import random

def jugar():
    #for rondas in range(1):
        print("\nplantilla")
        # guardados = guardar_dados()
        # for turnos in range(3):
        #     print(f"\nTurno {turnos + 1}")
        tirada()

def tirada(lista):
    lista_dados = []
    inicio_caras = 1
    fin_caras = 6
    for turnos in range(3):
        print(f"\nTurno {turnos + 1}")
        for _ in range(5):
            dado = random.randint(inicio_caras, fin_caras)
            lista_dados.append(dado)
        print(lista_dados)
        guardar_dados(lista_dados)


def guardar_dados(lista):
    dados_guardados = []
    
    pedido = input("Elige la posicion de los dados a guardar: ").split(',')
    
    for i in range(len(lista)):
        for x in pedido:
            if int(x) == i:
                dados_guardados.append(lista[i])
    print(dados_guardados)
    return dados_guardados