import random
import calculos as calc
import validaciones as val

def jugar():
    puntajes = {"uno": 0,
                "dos": 0,
                "tres": 0,
                "cuatro": 0,
                "cinco": 0,
                "seis": 0,
                "escalera": 0,
                "full": 0,
                "poker": 0,
                "generala": 0}
    
    vueltas = 3
    for rondas in range(vueltas):
        guardar_jugadas = []
        plantilla(puntajes)

        print(f"\n{'':>15}=== RONDA {rondas + 1} - Rondas restantes: {vueltas - rondas - 1} ===")
        for turnos in range(3):
            print("\n" + "-"*70)
            print(f"TURNO {turnos + 1}")
            tirada(guardar_jugadas)
            if turnos != 2:
                print("-"*70)
                guardar_jugadas = guardar_dados(guardar_jugadas)
        
            if len(guardar_jugadas) == 5:
                break
        
        puntajes = posibles_jugadas(guardar_jugadas,puntajes)

def plantilla(puntajes):
    print("\n" + "-"*26)
    print("\tPLANTILLA")
    print("-"*26)
    print(f"{'[Uno]'} {puntajes["uno"]:>11}\n"
        f"{'[Dos]'} {puntajes["dos"]:>11}\n"
        f"{'[Tres]'} {puntajes["tres"]:>11}\n"
        f"{'[Cuatro]'} {puntajes["cuatro"]:>11}\n"
        f"{'[Cinco]'} {puntajes["cinco"]:>11}\n"
        f"{'[Seis]'} {puntajes["seis"]:>11}\n"
        f"{'[Escalera]':<0} {puntajes["escalera"]:>11}\n"
        f"[Full] {puntajes["full"]:>15}\n"
        f"[Poker] {puntajes["poker"]:>14}\n"
        f"[Generala] {puntajes["generala"]:>11}")
    print("-"*26)
    print(f"Total {'-':>16}")
    print("-"*26)
    return    

def tirada(lista):
    dados = 5
    inicio_caras = 1
    fin_caras = 6
    emblemas = {1: "Simbolo 1",
                2: "Simbolo 2",
                3: "Simbolo 3",
                4: "Simbolo 4",
                5: "Simbolo 5",
                6: "Simbolo 6"}
    
    for _ in range(dados - len(lista)):
        valor = random.randint(inicio_caras, fin_caras)
        lista.append(valor)

    print(f"Posicion:", end=' ')
    for q in range(dados):
        if q != 4:
            print(f"[{q + 1:^7}]", end=" - ")
        else:
            print(f"[{q + 1:^7}]")

    print(f"Simbolo:{' ':>1}", end=' ')
    for y in range(len(lista)):
        if y != 4:
            print(f"{emblemas[lista[y]]:<10}", end="| ")
        else:
            print(f"{emblemas[lista[y]]}")

    print(f"Valor:{' ':>6}", end=' ')
    for e in range(dados):
        if e != 4:
            print(f"({lista[e]}){'':^9}", end="")
        else:
            print(f"({lista[e]}){'':^9}")
    return   


def guardar_dados(jugada):
    dados_guardados = []
    
    pedido = input("\nElige la posicion de los dados a guardar: ").strip()
    if pedido == "":
        return dados_guardados
    
    for x in pedido.split(','):
        dados_guardados.append(jugada[int(x) - 1])
    dados_guardados.sort()
    return dados_guardados
    

def posibles_jugadas(lista,puntajes_guardados):
    jugadas_posibles = {"1": 0,
                        "2": 0,
                        "3": 0,
                        "4": 0,
                        "5": 0,
                        "6": 0,
                        "7": 0,
                        "8": 0,
                        "9": 0,
                        "10": 0}

    calc.caras(lista, jugadas_posibles, puntajes_guardados)
    calc.escalera(lista, jugadas_posibles, puntajes_guardados)
    calc.full(lista, jugadas_posibles, puntajes_guardados)
    calc.poker(lista, jugadas_posibles, puntajes_guardados)
    calc.generala(lista, jugadas_posibles, puntajes_guardados)

    print("\n" + "-"*26)
    print(f"{'POSIBLES JUGADAS':^27}")
    print("-"*26)
    print(f"[1] Uno: {jugadas_posibles['1']:>14}\n"
          f"[2] Dos: {jugadas_posibles['2']:>14}\n"
          f"[3] Tres: {jugadas_posibles['3']:>13}\n"
          f"[4] Cuatro: {jugadas_posibles['4']:>11}\n"
          f"[5] Cinco: {jugadas_posibles['5']:>12}\n"
          f"[6] Seis: {jugadas_posibles['6']:>13}\n"
          f"[7] Escalera: {jugadas_posibles['7']:>9}\n"
          f"[8] Full: {jugadas_posibles['8']:>13}\n"
          f"[9] Poker: {jugadas_posibles['9']:>12}\n"
          f"[10] Generala: {jugadas_posibles['10']:>8}")
    
    while True:
        opcion = input("\nElige la jugada a puntuar: ")
        validar = val.validar_puntaje(opcion, puntajes_guardados, jugadas_posibles)
        
        if validar:
            break
    return puntajes_guardados

    
    



        