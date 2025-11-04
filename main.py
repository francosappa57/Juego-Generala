import funciones

while True:
    print("-" * 15)
    print("MINI GENERALA")
    print("-" * 15)
    print("1. Jugar\n"
          "2. Estadisticas\n"
          "3. Creditos\n"
          "4. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        funciones.jugar()
    # elif opcion == "2":
    #     pass
    # elif opcion == "3":
    #     pass
    elif opcion == "4":
        break
    else:
        print("Opcion incorrecta. Intenmtar nuevamente")