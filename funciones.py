import random
import calculos as calc

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
        #calcular_jugada(guardar_jugadas)
        posibles_jugadas(guardar_jugadas)


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
    # for i in range(5):
    #     lista.append(i + 1)
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
    dados_guardados.sort()
    return dados_guardados
    

def posibles_jugadas(lista):
    print("\n" + "-"*26)
    print(f"{'POSIBLES JUGADAS':^27}")
    print("-"*26)
    puntajes = calc.caras(lista)
    # contador = 1
    # for clave, valor in puntajes.items():
    #     print(f"[{contador}] {clave.capitalize()}: {valor}")
    #     contador += 1
    print(f"[1] Uno: {puntajes['uno']:>14}\n"
          f"[2] Dos: {puntajes['dos']:>14}\n"
          f"[3] Tres: {puntajes['tres']:>13}\n"
          f"[4] Cuatro: {puntajes['cuatro']:>11}\n"
          f"[5] Cinco: {puntajes['cinco']:>12}\n"
          f"[6] Seis: {puntajes['seis']:>13}\n"
          f"[7] Escalera: {calc.escalera(lista):>9}\n"
          f"[8] Full: {calc.full(lista):>13}\n"
          f"[9] Poker: {calc.poker(lista):>12}\n"
          f"[10] Generala: {calc.generala(lista):>8}\n")
    
    opcion = input("Elige la jugada a puntuar: ")
    
    



        