import random
import calculos.calculos as calc
import validaciones.validaciones as val
import archivos.archivos as ar
import json

#archivo_tematica = "archivos/tematica.json"
archivo = "mejores_puntajes.csv"

def jugar():
    """
        Funcion principal del juego, se encarga de iniciar los puntajes, las rondas y los turnos.
        Encargarda de llamar a las demas funciones

    """
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
    primero = False
    total = 0 
    for rondas in range(vueltas):
        guardar_jugadas = []
        plantilla(puntajes, total)
        
        print(f"\n{'':>15}=== RONDA {rondas + 1} - Rondas restantes: {vueltas - rondas - 1} ===")
        for turnos in range(3):
            print("\n" + "-"*70)
            print(f"TURNO {turnos + 1}")
            tirada(guardar_jugadas)
            if turnos != 2:
                print("-"*70)
                guardar_jugadas = guardar_dados(guardar_jugadas)
                
            if len(guardar_jugadas) == 5 and rondas == 0 and turnos == 0:
                primero = calc.generala(guardar_jugadas,puntajes)
                break
            elif len(guardar_jugadas) == 5:
                break
        
        if primero:
            puntajes["generala"] = 1000
            puntaje_maximo = calc.calcular_total(puntajes)
            plantilla(puntajes, puntaje_maximo)
            print(f"\nGANASTE - PUNTAJE TOTAL: {puntaje_maximo}")
            break
        
        puntajes = posibles_jugadas(guardar_jugadas,puntajes)
        total = calc.calcular_total(puntajes)
    print(f"\nGANASTE - PUNTAJE TOTAL: {total}")
    ar.ingresa_ganador(archivo, total)

def plantilla(puntajes, total):
    """
        Imprime la plantilla de puntajes del jugador
    """
    print("\n" + "-"*26)
    print(f"{"PLANTILLA":^25}")
    print("-"*26)
    print(f"[Uno]: {puntajes["uno"]:>15}\n"
          f"[Dos]: {puntajes["dos"]:>15}\n"
          f"[Tres]: {puntajes["tres"]:>14}\n"
          f"[Cuatro]: {puntajes["cuatro"]:>12}\n"
          f"[Cinco]: {puntajes["cinco"]:>13}\n"
          f"[Seis]: {puntajes["seis"]:>14}\n"
          f"[Escalera]: {puntajes["escalera"]:>10}\n"
          f"[Full]: {puntajes["full"]:>14}\n"
          f"[Poker]: {puntajes["poker"]:>13}\n"
          f"[Generala]: {puntajes["generala"]:>10}")
    print("-"*26)
    print(f"Total {total:>16}")
    print("-"*26)
    return    


def tirada(lista):
    """
        Genera los valores de la tirada de dados con sus respectivos emblemas
    """
#    with open(archivo_tematica) as archivo:
#        diccionario_emblemas= json.load(archivo)
    dados = 5
    inicio_caras = 1
    fin_caras = 6
#    emblemas = diccionario_emblemas["tematicas"]
    emblemas = {1: "Simbolo 1",
                2: "Simbolo 2",
                3: "Simbolo 3",
                4: "Simbolo 4",
                5: "Simbolo 5",
                6: "Simbolo 6"}
    
    for _ in range(dados - len(lista)):
        valor = random.randint(inicio_caras, fin_caras)
        lista.append(valor)

    # numero = [5, 5, 5, 2, 2]
    # for i in numero:
    #     lista.append(i)

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
    """
        guarda los valores que el usuario quiera en cada tirada
    """
    while True:
        dados_guardados = []
        pedido = input("\nEligir dados a guardar(segun la posicion y separados por comas) o presionar ENTER para no guardar dados: ").strip()
        if pedido == "":
            return dados_guardados
    
        for x in pedido.split(','):
            if val.validacion_guardado(x) == False:
                break  
            elif pedido.count(str(x)) > 1 :
                print("\nNo se pueden repetir numeros")
                break  
            dados_guardados.append(jugada[int(x) - 1])
        if len(pedido.split(',')) != len(dados_guardados):
            print("\nPosiciones incorrectas.")
        else:
            dados_guardados.sort()
            return dados_guardados
    

def posibles_jugadas(lista,puntajes_guardados):
    """
        permite al usuario ver y elegir las jugadas disponibles dependiendo de los valores que saco en la tirada
    """
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
    calc.generala(jugadas_posibles, puntajes_guardados, lista)

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
        opcion = input("\nElegir jugada a puntuar o eliminar(jugadas con 0 puntos): ").strip()
        if val.validar_posible_jugada(opcion) == False:
            print(f"\nOpcion invalida")
        else:
            validar = val.validar_puntaje(opcion, puntajes_guardados, jugadas_posibles)
            eliminar_jugada(validar, puntajes_guardados)
            if validar:
                break
    return puntajes_guardados


def eliminar_jugada(eliminar,puntajes):
    """
        Elimina jugadas de la planilla
    """
    if eliminar in puntajes.keys():
        puntajes[eliminar] = "-"
        return
    return

    
    



        