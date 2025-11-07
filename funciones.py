import random
import calculos as calc

def jugar():
    puntajes = None
    contador = 1
    for rondas in range(contador):
        guardar_jugadas = []
        if puntajes == None:
            plantilla(puntajes)
        else:
            plantilla(puntajes)
        # print("\n" + "-"*26)
        # print("\tPLANTILLA")
        # print("-"*26)
        # for i in range(6):
        #     print(f"[{i + 1}] {'-':>18}")   
        # print(f"{'[Escalera]':<0} {'-':>11}\n"
        #       f"[Full] {'-':>15}\n"
        #       f"[Poker] {'-':>14}\n"
        #       f"[Generala] {'-':>11}")
        # print("-"*26)
        # print(f"Total {'-':>16}")
        # print("-"*26)
        
        print(f"\n=== RONDA {rondas + 1} - Rondas restantes: {contador - rondas - 1} ===")
        for turnos in range(3):
            print(f"\nTurno {turnos + 1}")
            tirada(guardar_jugadas)
            if turnos != 2:
                guardar_jugadas = guardar_dados(guardar_jugadas)
        
            if len(guardar_jugadas) == 5:
                break
        #calcular_jugada(guardar_jugadas)
        puntajes = posibles_jugadas(guardar_jugadas,puntajes)

def plantilla(puntajes):
    if puntajes == None:
        puntajes_guardados = {"uno": 0,
                            "dos": 0,
                            "tres": 0,
                            "cuatro": 0,
                            "cinco": 0,
                            "seis": 0,
                            "escalera": 0,
                            "full": 0,
                            "poker": 0,
                            "generala": 0}

    print("\n" + "-"*26)
    print("\tPLANTILLA")
    print("-"*26)
    print(f"{'[unos]'} {puntajes_guardados["uno"]:>11}\n"
            f"{'[doses]'} {puntajes_guardados["dos"]:>11}\n"
            f"{'[treses]'} {puntajes_guardados["tres"]:>11}\n"
            f"{'[cuatros]'} {puntajes_guardados["cuatro"]:>11}\n"
            f"{'[cincos]'} {puntajes_guardados["cinco"]:>11}\n"
            f"{'[seises]'} {puntajes_guardados["seis"]:>11}\n"
            f"{'[escalera]':<0} {puntajes_guardados["escalera"]:>11}\n"
            f"[full] {puntajes_guardados["full"]:>15}\n"
            f"[poker] {puntajes_guardados["poker"]:>14}\n"
            f"[generala] {puntajes_guardados["generala"]:>11}")
    print("-"*26)
    print(f"Total {'-':>16}")
    print("-"*26)
    return puntajes_guardados    

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
    

def posibles_jugadas(lista,puntajes_guardados):
    print (puntajes_guardados)
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
    while True:
        opcion = int(input("Elige la jugada a puntuar: "))

        if opcion == 1:
            if puntajes_guardados ['uno'] == 0:
                puntajes_guardados['uno'] = puntajes['uno']
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 2:
            if puntajes_guardados ['dos'] == 0:
                puntajes_guardados['dos'] = puntajes['dos']
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 3:
            if puntajes_guardados ['tres'] == 0:
                puntajes_guardados['tres'] = puntajes['tres']
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 4:
            if puntajes_guardados ['cuatro'] == 0:
                puntajes_guardados['cuatro'] = puntajes['cuatro']
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 5:
            if puntajes_guardados ['cinco'] == 0:
                puntajes_guardados['cinco'] = puntajes['cinco']
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 6:
            if puntajes_guardados ['seis'] == 0:
                puntajes_guardados['seis'] = puntajes['seis']
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 7:
            if puntajes_guardados ['escalera'] == 0:
                puntajes_guardados['escalera'] = calc.escalera(lista)
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 8:
            if puntajes_guardados ['full'] == 0:
                puntajes_guardados['full'] = calc.full(lista)
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 9:
            if puntajes_guardados ['poker'] == 0:
                puntajes_guardados['poker'] = calc.poker(lista)
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        elif opcion == 10:
            if puntajes_guardados ['generala'] == 0:
                puntajes_guardados['generala'] = calc.generala(lista)
                break
            else:
                print ("Ese valor ya fue guardado antes...")
        else:
            print ("Opcion invalida")
    return puntajes_guardados

    
    



        