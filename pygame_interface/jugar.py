import pygame
from pygame_interface.gui import crear_boton, dibujar_boton, boton_clickeado
from funciones.funciones import jugar, posibles_jugadas, guardar_dados, tirada
from calculos.calculos import calcular_total, generala, poker, full, escalera, caras

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

def py_jugar(pantalla, font):
    #config
    pygame.mixer.music.load("assets/OST/1-49. Game Corner.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    pantalla.blit(fondo, (0,0))
    # inicio de variables
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
        if ronda_actual > TOTAL_RONDAS:
            print ("fin")
            return "Menu"

        if vueltas_restantes < VUELTAS_POR_RONDA and dados_actuales:
            guardar_jugadas = [dados_actuales[i] for i in dados_seleccionados_posiciones]
        else:
            dados_seleccionados_posiciones = []
            if vueltas_restantes == VUELTAS_POR_RONDA:
                 dados_seleccionados_posiciones = []

        #puntajes = py_planilla(dados_actuales, puntajes)
        #py_planilla_botones(pantalla, font, puntajes)
        tirar_dados = pygame.Rect(150, 530, 170, 50)
        pygame.draw.rect(pantalla, (150,0,0), tirar_dados )
        pantalla.blit(font.render("Tirar dados", True, (0,0,0)),(150, 530, 170, 50))
        pantalla.blit(font.render(f"RONDA {ronda_actual}/{TOTAL_RONDAS}", True, (250, 250, 250)), (125, 30))
        pantalla.blit(font.render(f"TIRADAS: {vueltas_restantes}/{VUELTAS_POR_RONDA}", True, (250, 250, 250)), (125, 450))
        jugada_elegida = None


        #espacio_dado_lista = []
        #dibujo dados
#            if dados_actuales:
#                py_planilla(pantalla, font, dados_actuales, puntajes)
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
#test
        #if jugada_elegida:
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
                        dados_actuales = tirada(guardar_jugadas)
                        vueltas_restantes -= 1
                        dados_seleccionados_posiciones = []
                        #test (no estoy seguro de ponerlo aca)
                        pantalla.blit(fondo, (0,0))
                    else:
                        print("Tiradas agotadas, debees seleccionar una jugada")
                puntajes_imp = py_planilla(dados_actuales, puntajes)
                posiciones_jugadas = py_planilla_botones(pantalla, font, puntajes_imp, puntajes)
                    
                for i ,jugada_rect in posiciones_jugadas.items():
                    if jugada_rect.collidepoint (mx,my):
                        print("entro")
                        puntajes[i] = puntajes_imp[i]
                        print(puntajes)
                        break

                # funcion para imprimir dado marcado
                
                for i, dado_rect in enumerate(espacio_dado_lista):
                    if dado_rect.collidepoint(mx,my):
                        dados_seleccionados_posiciones = guardar_dados_py(pantalla,dado_rect,i, dados_seleccionados_posiciones)
                        break    

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
    
def py_planilla_botones(pantalla, font, jugadas_posibles, puntajes):
    posiciones = [
        (550, 185), (550, 240), (550, 295), (550, 350), (550, 405), (550, 460),
        (700, 185), (700, 240), (700, 295), (700, 350)]
    
    botones_rects = {}
    for i, (x, y) in enumerate(posiciones):
        # if i+1 == 7:
        #     clave_jugada = 'escalera'
        # elif i+1 == 8:
        #     clave_jugada = 'full'
        # elif i+1 == 9:
        #     clave_jugada = 'poker'
        # elif i+1 == 10:
        #     clave_jugada = 'generala'
        # else:          
        clave_jugada = str (i+1)
        if clave_jugada == "7":
            puntajes["escalera"] = jugadas_posibles[clave_jugada]
            clave = 'escalera'
        elif clave_jugada == "8":
            puntajes["full"] = jugadas_posibles[clave_jugada]
            clave = 'full'
        elif clave_jugada == "9":
            puntajes["poker"] = jugadas_posibles[clave_jugada]
            clave = 'poker'
        elif clave_jugada == "10":
            puntajes["generala"] = jugadas_posibles[clave_jugada]
            clave = 'generala'
        else:
            puntajes[clave_jugada] = jugadas_posibles[clave_jugada]
        #puntaje = jugadas_posibles[clave_jugada]

        #dibuja boton
        rect_boton = pygame.Rect(x, y, 60, 30)
        pygame.draw.rect(pantalla,(245,218,127), rect_boton)

        #dibuja texto
        texto_superficie = font.render(str(jugadas_posibles[clave_jugada]), True, (0,0,0))
        texto_rect = texto_superficie.get_rect(center=rect_boton.center)
        pantalla.blit(texto_superficie, texto_rect)
        botones_rects[clave_jugada] = rect_boton
        print (botones_rects)
    
    return botones_rects
    
    #for nombre,x,y in posiciones_dibujadas():
    #    pantalla.blit(font.render(nombre, True, ((0,0,0))), (x, y))

    #unos_bton = pygame.Rect(550, 185, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), unos_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["1"]}", True, ((0,0,0))), (550, 185))
    #unos_bton = crear_boton(f"{jugadas_posibles["1"]}",550, 185, 60, 30)
    #dibujar_boton(pantalla, unos_bton, font)
    #if boton_clickeado(evento, unos_bton):

    #doses_bton = pygame.Rect(550, 240, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), doses_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["2"]}", True, ((0,0,0))), (550, 240))
    
    #treses_bton = pygame.Rect(550, 295, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), treses_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["3"]}", True, ((0,0,0))), (550, 295))
    
    #cuatros_bton = pygame.Rect(550, 350, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), cuatros_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["4"]}", True, ((0,0,0))), (550, 350))

    #cincos_bton = pygame.Rect(550, 405, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), cincos_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["5"]}", True,((0,0,0))), (550, 405))

    #seises_bton = pygame.Rect(550, 460, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), seises_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["6"]}", True, ((0,0,0))), (550, 460))

    #escalera_bton = pygame.Rect(700, 185, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), escalera_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["7"]}", True, ((0,0,0))), (700, 185))

    #full_bton = pygame.Rect(700, 240, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), full_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["8"]}", True, ((0,0,0))), (700, 240))

    #poker_bton = pygame.Rect(700, 295, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), poker_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["9"]}", True, ((0,0,0))), (700, 295))

    #generala_bton = pygame.Rect(700, 350, 60, 30)
    #pygame.draw.rect(pantalla, (245,218,127), generala_bton )
#    pantalla.blit(font.render(f"{jugadas_posibles["10"]}", True, ((0,0,0))), (700, 350))





def guardar_dados_py(pantalla, dado_rect, posicion_dado, dados_seleccionados_posiciones):
    img_seleccion = pygame.transform.scale(imagenes_dados[6], (100, 100))         
#    pantalla.blit(img_seleccion, dado)
    print(f"dado {posicion_dado}")
    if posicion_dado in dados_seleccionados_posiciones:
        print(f"Dado en posición {posicion_dado} removido.")
        dados_seleccionados_posiciones.remove(posicion_dado)
    else:
        print(f"Dado en posición {posicion_dado} añadido.")
        dados_seleccionados_posiciones.append(posicion_dado)        
        pantalla.blit(img_seleccion, dado_rect)
    print(f"Seleccionados: {dados_seleccionados_posiciones}")
    return dados_seleccionados_posiciones
