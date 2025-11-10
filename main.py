import funciones.funciones as ff
from archivos.arch_csv.archivos_csv import ingresa_ganador, ver_estadisticas
from archivos.arch_json.archivo_json import guaradar_json
archivo_juego_csv = "archivos/arch_csv/puntajes.csv"
archivo_juego_json = "config.json"

while True:
    print("\n--- MINI GENERALA ---")
    print("1. Jugar\n"
          "2. Estadísticas\n"
          "3. Créditos\n"
          "4. Salir")
    opcion = input("Elige una opción: ")
    guaradar_json(archivo_juego_json)
    
    if opcion == "1":
        puntaje_final = ff.jugar()
        ingresa_ganador(archivo_juego_csv, puntaje_final)
    elif opcion == "2":
        ver_estadisticas(archivo_juego_csv)
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