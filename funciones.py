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
    posicion= [1,2,3,4,5]
    simbolo= []
    emblemas = ["Simbolo 1 (1)", "Simbolo 2 (2)", "Simbolo 3 (3)", "Simbolo 4 (4)", "Simbolo 5 (5)", "Simbolo 6 (6)"]
    for _ in range(dados - len(lista)):
        valor = random.randint(inicio_caras, fin_caras)
        lista.append(valor)
    for y in lista:
        simbolo.append(emblemas[y-1])
    print(f"Posicion: {posicion}")
    print(f"Simbolo{' ':>1}: {simbolo}")
    print(f"Valor{' ':>3}: {lista}")
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
    jugadas = [{"uno": puntaje}]
    conjunto_dados = set(lista)
    #nueva_lista = list(conjunto_dados)
    # lista.sort()
    print(lista)
    
    for x in conjunto_dados:
        puntaje = lista.count(x) * x
        jugadas.add()
        if lista.count(x) == 4:
            poker = 40
        if lista.count(x) == 5:
            generala = 50
        if lista.count(x) == 1:
            total = 0
            total += x
            if total == 15 or total == 20:
                escalera = 20

    full = 0
    for i in conjunto_dados:
        if lista.count(i) == 3:
            full += 3
        else:
            full += 2
    if full == 5:
        puntaje = 30

    print("\n--- Jugadas disponibles ---")
    for i in range(len(jugadas)):
        print(f"[{i + 1}] - {jugadas[i]}: -")
    



        