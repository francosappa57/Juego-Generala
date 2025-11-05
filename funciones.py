import random

def jugar():
    for rondas in range(2):
        guardar_jugadas = []
    
        print("\n" + "-"*26)
        print("\tPLANTILLA")
        print("-"*26)
        for i in range(6):
            print(f"[{i + 1}] {'-':>18}")   
        print(f"{'[Escalera]':<0} {'-':>11}\n"
              f"[Full] {'-':>15}\n"
              f"[Poker] {'-':>14}\n"
              f"[Generala] {'-':>11}")
        print("-"*26)
        print(f"Total {'-':>16}")
        print("-"*26)
        
        for turnos in range(3):
            print(f"\nTurno {turnos + 1}")
            jugada = tirada(guardar_jugadas)
            if turnos != 2:
                valor_dados = guardar_dados(jugada)
                if len(valor_dados) != 0:    
                    for i in valor_dados:
                        guardar_jugadas.append(i)
            
            if len(guardar_jugadas) == 5:
                break
        calcular_jugada(guardar_jugadas)
    #       print(guardados)

def tirada(lista):
    lista_dados = []
    if len(lista) > 0:
        for v in lista:
            lista_dados.append(v)
    dados = 5
    inicio_caras = 1
    fin_caras = 6
    for _ in range(dados - len(lista)):
        valor = random.randint(inicio_caras, fin_caras)
        lista_dados.append(valor)
    print(lista_dados)
    return lista_dados    


def guardar_dados(lista):
    dados_guardados = []

    pedido = input("Elige la posicion de los dados a guardar: ")

    if pedido == "":
        return dados_guardados
    else:
        for i in range(len(lista)):
            for x in pedido.split(','):
                if int(x) == i + 1:
                    dados_guardados.append(lista[i])
    return dados_guardados


def calcular_jugada(lista):
    jugadas = ("1","2","3","4","5","6","Escalera","Full","Poker","Generala")
    
    
    print("\n--- Jugadas disponibles ---")
    for i in range(len(jugadas)):
        print(f"[{i + 1}] - {jugadas[i]}: -")   
    
    pass