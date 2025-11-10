import funciones.funciones as ff
import archivos.archivos as arch
archivo = "archivos/mejores_puntajes.csv"

while True:
    #print("-" * 15)
    print("\n--- MINI GENERALA ---")
    #print("-" * 15)
    print("1. Jugar\n"
          "2. Estadísticas\n"
          "3. Créditos\n"
          "4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        ff.jugar()
    elif opcion == "2":
        arch.ver_ganadores(archivo)
    elif opcion == "3":
        print("#" * 35)
        print(f"{'MINI GENERALA':>10}")
        print("#" * 35)
        print(f"Autor/es: Franco Sappa - Luciano Nicolas Torres Tonkowicz\n"
               "Fecha: 4/11\n"
               "Materia: programación I\n"
               "Docentes: Martín Alejandro García - Verónica Natalia Carbonari\n"
               "Carrera: Tecnicatura en programación\n"
               "Contacto: sappa57@gmail.com - luciano.torres883@gmail.com")
        print("#" * 35)

    elif opcion == "4":
        break
    else:
        print("Opcion incorrecta. Intenmtar nuevamente")