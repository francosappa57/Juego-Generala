import pygame
from pygame_interface.gui import crear_boton, dibujar_boton, boton_clickeado
from funciones.funciones import jugar, posibles_jugadas, guardar_dados, tirada, eliminar_jugada
from calculos.calculos import calcular_total, generala, poker, full, escalera, caras
from validaciones.validaciones import validar_puntaje

imagenes_dados = [
    pygame.image.load("assets/UI/Dices/Bulbasaur_1.png"),
    pygame.image.load("assets/UI/Dices/Charmander_2.png"),
    pygame.image.load("assets/UI/Dices/Squirtle_3.png"),
    pygame.image.load("assets/UI/Dices/Pikachu_4.png"),
    pygame.image.load("assets/UI/Dices/Nidoking_5.png"),
    pygame.image.load("assets/UI/Dices/Blaziken_6.png"),
    pygame.image.load("assets/UI/Dices/Selector.png")
]

fondo = pygame.image.load("assets/UI/Menu_jugar.png")

clock = pygame.time.Clock()
def py_jugar(pantalla, font):
    #config
    pygame.mixer.music.load("assets/OST/1-49. Game Corner.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    pantalla.blit(fondo, (0,0))
    # inicio de variables
    tirar_dados = pygame.Rect(150, 530, 170, 50)
    dados_seleccionados_posiciones = []
    dados_actuales = []
    guardar_jugadas = []
    TOTAL_RONDAS = 10
    VUELTAS_POR_RONDA = 3
    vueltas_restantes = VUELTAS_POR_RONDA
    ronda_actual = 1

    puntajes = {"1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "escalera": 0,
                "full": 0,
                "poker": 0,
                "generala": 0}

    # Inicio de ciclo de pygame
    while True:
        clock.tick(60)
        if ronda_actual > TOTAL_RONDAS:
            print ("fin")
            return "Menu"

        if vueltas_restantes < VUELTAS_POR_RONDA and dados_actuales:
            guardar_jugadas = [dados_actuales[i] for i in dados_seleccionados_posiciones]
        else:
            if vueltas_restantes == VUELTAS_POR_RONDA:
                dados_seleccionados_posiciones = []

        #puntajes = py_planilla(dados_actuales, puntajes)
        #py_planilla_botones(pantalla, font, puntajes)
            
        txt_tirar = font.render("Tirar dados", True, (0,0,0))
        txt_tirada = font.render(f"TIRADAS: {vueltas_restantes}/{VUELTAS_POR_RONDA}", True, (250, 250, 250))
        txt_ronda = font.render(f"RONDA: {ronda_actual}/{TOTAL_RONDAS}", True, (250, 250, 250))
        total = calcular_total(puntajes)
        txt_total = font.render(f"{total}", True, (0,0,0))
        
        pygame.draw.rect(pantalla, (150,0,0), tirar_dados)
        
        pantalla.blit(txt_tirar, txt_tirar.get_rect(center=tirar_dados.center))
        pantalla.blit(txt_tirada, (125, 450))
        pantalla.blit(txt_ronda, (125, 30))
        pantalla.blit(txt_total, (570, 540))
        jugada_elegida = None


        espacio_dado_lista = []
        if dados_actuales:
            x_base = 50
            y_base = 150
            sep_horizontal= 120
            sep_vertical= 130

            for i, valor in enumerate(dados_actuales):
                img = imagenes_dados[valor - 1]
                img_achicada = pygame.transform.scale(img, (100, 100))
                if i < 3:
                    x_pos = x_base + i * sep_horizontal
                    y_pos = y_base
                elif i == 3:
                    x_pos = x_base + (i - 2) * sep_horizontal / 2
                    y_pos = y_base + sep_vertical
                else:
                    x_pos = x_base + (i - 3) * sep_horizontal + 75
                    y_pos = y_base + sep_vertical
                espacio_dado = img_achicada.get_rect(topleft=(x_pos, y_pos))
                espacio_dado_lista.append(espacio_dado)
                pantalla.blit(img_achicada, (x_pos, y_pos))

                # dibuja el selector si se encuentra dentro de la lista
                if i in dados_seleccionados_posiciones:
                    img_seleccion = pygame.transform.scale(imagenes_dados[6], (100, 100))
                    pantalla.blit(img_seleccion, espacio_dado)
                
        # if jugada_elegida:
        #    print(f"Jugada elegida: {jugada_elegida}. Pasa a la Ronda {ronda_actual + 1}.")
        #    ronda_actual += 1
        #    vueltas_restantes = VUELTAS_POR_RONDA # Reinicia las tiradas
        #    dados_actuales = [] # Limpia los dados
        #    dados_seleccionados_posiciones = [] # Limpia la selección
        #    jugada_elegida = None # Reset flag

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if tirar_dados.collidepoint(mx, my):
                    if vueltas_restantes > 0:
                        vueltas_restantes -= 1
                        dados_actuales = tirada(guardar_jugadas)
                        # pantalla.blit(fondo, (0,0))                  
                    else:
                        print("Tiradas agotadas, debees seleccionar una jugada")


                puntajes_imp = py_planilla(dados_actuales, puntajes)
                posiciones_jugadas = py_planilla_botones(pantalla, font, puntajes_imp)


                for i, dado_rect in enumerate(espacio_dado_lista):
                    if dado_rect.collidepoint(mx,my):
                        dados_seleccionados_posiciones = guardar_dados_py(pantalla,dado_rect,i, dados_seleccionados_posiciones)
                
                

                for i ,jugada_rect in posiciones_jugadas.items():
                    if jugada_rect.collidepoint (mx,my):
                        print("entro")
                        validar = validar_puntaje(i, puntajes, puntajes_imp)
                        eliminar_jugada(validar, puntajes)
                        if validar:
                            ronda_actual += 1
                            vueltas_restantes = VUELTAS_POR_RONDA
                            dados_actuales = []
                            guardar_jugadas = []
                        pantalla.blit(fondo, (0,0))
            
            
        pygame.display.flip()

        def py_planilla(lista, puntajes_guardados):
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
                
                caras(lista, jugadas_posibles, puntajes_guardados)
                escalera(lista, jugadas_posibles, puntajes_guardados)
                full(lista, jugadas_posibles, puntajes_guardados)
                poker(lista, jugadas_posibles, puntajes_guardados)
                generala(jugadas_posibles, puntajes_guardados, lista)
                return jugadas_posibles

                
        def py_planilla_botones(pantalla, font, jugadas_posibles):
            posiciones = [
                (550, 185), (550, 240), (550, 295), (550, 350), (550, 405), (550, 460),
                (700, 185), (700, 240), (700, 295), (700, 350)]
            
            botones_rects = {}
            for i, (x, y) in enumerate(posiciones):
                clave_jugada = str(i+1)          
                puntaje = jugadas_posibles[clave_jugada]

                #dibuja boton
                rect_boton = pygame.Rect(x, y, 60, 30)
                pygame.draw.rect(pantalla,(245,218,127), rect_boton)

                #dibuja texto
                texto_superficie = font.render(str(puntaje), True, (0,0,0))
                texto_rect = texto_superficie.get_rect(center=rect_boton.center)
                pantalla.blit(texto_superficie, texto_rect)
                botones_rects[clave_jugada] = rect_boton
            
            return botones_rects


def guardar_dados_py(pantalla, dado_rect, posicion_dado, dados_seleccionados_posiciones):
    img_seleccion = pygame.transform.scale(imagenes_dados[6], (100, 100))         
#    pantalla.blit(img_seleccion, dado)
    # print(f"dado {posicion_dado}")
    if posicion_dado in dados_seleccionados_posiciones:
        # print(f"Dado en posición {posicion_dado} removido.")
        dados_seleccionados_posiciones.remove(posicion_dado)
    else:
        # print(f"Dado en posición {posicion_dado} añadido.")
        dados_seleccionados_posiciones.append(posicion_dado)        
        pantalla.blit(img_seleccion, dado_rect)
    # print(f"Seleccionados: {dados_seleccionados_posiciones}")
    return dados_seleccionados_posiciones
