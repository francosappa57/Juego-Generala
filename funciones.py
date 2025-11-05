import random

def jugar():
    contador = 1
    for rondas in range(contador):
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
        
        print(f"\n=== RONDA {rondas + 1} - Rondas restantes: {contador - rondas - 1} ===")
        for turnos in range(3):
            print(f"\nTurno {turnos + 1}")
            tirada(guardar_jugadas)
            if turnos != 2:
                guardar_jugadas = guardar_dados(guardar_jugadas)
        
            if len(guardar_jugadas) == 5:
                break
        calcular_jugada(guardar_jugadas)


def tirada(lista):
    dados = 5
    inicio_caras = 1
    fin_caras = 6
    for _ in range(dados - len(lista)):
        valor = random.randint(inicio_caras, fin_caras)
        lista.append(valor)
    print(lista)
    return   


def guardar_dados(jugada):
    dados_guardados = []
    
    pedido = input("Elige la posicion de los dados a guardar: ").strip()
    if pedido == "":
        return dados_guardados
    
    for x in pedido.split(','):
        dados_guardados.append(jugada[int(x) - 1])
    return dados_guardados
    


def calcular_jugada(lista):
    jugadas = ("1","2","3","4","5","6","Escalera","Full","Poker","Generala")
    lista.sort()
    
    print(lista)
        
    
    # print("\n--- Jugadas disponibles ---")
    # for i in range(len(jugadas)):
    #     print(f"[{i + 1}] - {jugadas[i]}: -")