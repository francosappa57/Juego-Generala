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
    pygame.image.load("assets/UI/Dices/Selector2.png")
]

fondo = pygame.image.load("assets/UI/Menu_jugar.png")
fondo_ganador= pygame.image.load("assets/UI/ganaste5.png")

clock = pygame.time.Clock()

def py_jugar(pantalla, font):
    #config
    pygame.mixer.music.load("assets/OST/1-49. Game Corner.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)
    # inicio de variables
    dados_seleccionados_posiciones = []
    dados_actuales = []
    guardar_jugadas = []
    TOTAL_RONDAS = 5
    VUELTAS_POR_RONDA = 3
    vueltas_restantes = VUELTAS_POR_RONDA
    ronda_actual = 1
    posiciones = [(550, 185), (550, 240), (550, 295), (550, 350), (550, 405), (550, 460), (700, 185), (700, 240), (700, 295), (700, 350)]
    botones_rects = {}
    puntajes_imp = {}
    primero = False
    tiro= False

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

    tirar_dados = pygame.Rect(145, 495, 170, 100)
    for i, (x, y) in enumerate(posiciones):
        clave_jugada = str(i+1)          
        boton = pygame.Rect(x, y, 60, 30)
        botones_rects[clave_jugada] = boton
    
    # Inicio de ciclo de pygame
    while True:
        clock.tick(60)
        
        if ronda_actual > TOTAL_RONDAS:
            pygame.mixer.music.load("assets/OST/10. Victory! (Trainer).mp3")
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(-1)
            pantalla.blit(fondo_ganador, (0,0))
            pantalla.blit(font.render(f"PUNTUACION: {total}", True, (250, 250, 250)), (270, 245))
            print ("fin")
            return "Menu"

        if vueltas_restantes < VUELTAS_POR_RONDA and dados_actuales:
            guardar_jugadas = [dados_actuales[i] for i in dados_seleccionados_posiciones]
        
       #pygame.draw.rect(pantalla, (150,0,0), tirar_dados)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.load("assets/OST/03. Title Screen.mp3")
                pygame.mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)
                return "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if tirar_dados.collidepoint(mx, my):
                    tiro= True
                    if vueltas_restantes == 0:
                        print("Tiradas agotadas, debees seleccionar una jugada")
                    elif vueltas_restantes > 0 and dados_seleccionados_posiciones:
                        dados_seleccionados_posiciones = []
                        vueltas_restantes -= 1
                        tirada(guardar_jugadas)
                        dados_actuales = guardar_jugadas
                    else:
                        vueltas_restantes -= 1
                        tirada(guardar_jugadas)
                        dados_actuales = guardar_jugadas
                        if len(dados_actuales) == 5 and ronda_actual == 1 and vueltas_restantes == 2:
                            primero = generala(dados_actuales,puntajes)
                                
                    
                if tiro:
                    puntajes_imp = py_planilla(dados_actuales, puntajes)

                    for i, dado_rect in enumerate(espacio_dado_lista):
                        if dado_rect.collidepoint(mx,my):
                            dados_seleccionados_posiciones = guardar_dados_py(i, dados_seleccionados_posiciones)
                        
                    
                    for i ,jugada_rect in botones_rects.items():
                        if jugada_rect.collidepoint (mx,my):
                            validar = validar_puntaje(i, puntajes, puntajes_imp)
                            eliminar_jugada(validar, puntajes)
                            if validar:
                                ronda_actual += 1
                                vueltas_restantes = VUELTAS_POR_RONDA
                                dados_actuales = []
                                guardar_jugadas = []
                                dados_seleccionados_posiciones = []
                                puntajes_imp = {}
                                tiro= False
                                print(puntajes)
                            
                        
    
        pantalla.blit(fondo, (0,0))
        
        txt_tirar = font.render("TIRAR", True, (250,250,250))
        txt_tirada = font.render(f"TIRADAS: {vueltas_restantes}/{VUELTAS_POR_RONDA}", True, (250, 250, 250))
        
        if ronda_actual > TOTAL_RONDAS:
            txt_ronda = font.render(f"RONDA: {TOTAL_RONDAS}/{TOTAL_RONDAS}", True, (250, 250, 250))
        else:    
            txt_ronda = font.render(f"RONDA: {ronda_actual}/{TOTAL_RONDAS}", True, (250, 250, 250))
        
        if not primero:
            total = calcular_total(puntajes)
            txt_total = font.render(f"{total}", True, (0,0,0))
            pantalla.blit(txt_total, (570, 540))
            
        pantalla.blit(txt_tirar, txt_tirar.get_rect(center=tirar_dados.center))
        pantalla.blit(txt_tirada, (125, 463))
        pantalla.blit(txt_ronda, (125, 30))

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
        
        if primero:
            puntajes["generala"] = 1000
            total = calcular_total(puntajes)
            txt_total = font.render(f"{total}", True, (0,0,0))
            pantalla.blit(txt_total, (570, 540))
            pygame.mixer.music.load("assets/OST/10. Victory! (Trainer).mp3")
            pygame.mixer.music.set_volume(0.05)
            pygame.mixer.music.play(-1)
            pantalla.blit(fondo_ganador, (0,0))
            pantalla.blit(font.render(f"PUNTUACION: {total}", True, (250, 250, 250)), (270, 245))
            print ("fin")
            return "Menu"

        
        if puntajes_imp:
            for i in puntajes_imp:
                pygame.draw.rect(pantalla,(245,218,127), botones_rects[i])
                if int(i) <= 6 and puntajes[i] != 0:
                    texto_superficie = font.render(str(puntajes[i]), True, (255,0,0))
                elif int(i) == 7:
                    if puntajes["escalera"] != 0:
                        texto_superficie = font.render(str(puntajes["escalera"]), True, (255,0,0))
                    else:
                        if puntajes_imp[i] != 0:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (10,171,0))
                        else:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (0,0,0))
                elif int(i) == 8:
                    if puntajes["full"] != 0:
                        texto_superficie = font.render(str(puntajes["full"]), True, (255,0,0))
                    else:
                        if puntajes_imp[i] != 0:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (10,171,0))
                        else:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (0,0,0))
                elif int(i) == 9:
                    if puntajes["poker"] != 0:
                        texto_superficie = font.render(str(puntajes["poker"]), True, (255,0,0))
                    else:
                        if puntajes_imp[i] != 0:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (10,171,0))
                        else:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (0,0,0))
                elif int(i) == 10:
                    if puntajes["generala"] != 0:
                        texto_superficie = font.render(str(puntajes["generala"]), True, (255,0,0))
                    else:
                        if puntajes_imp[i] != 0:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (10,171,0))
                        else:
                            texto_superficie = font.render(str(puntajes_imp[i]), True, (0,0,0))
                else:
                    if puntajes_imp[i] != 0:
                        texto_superficie = font.render(str(puntajes_imp[i]), True, (10,171,0))
                    else:
                        texto_superficie = font.render(str(puntajes_imp[i]), True, (0,0,0))
                texto_rect = texto_superficie.get_rect(center=botones_rects[i].center) 
                pantalla.blit(texto_superficie, texto_rect)
                    

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

       

def guardar_dados_py(posicion_dado, dados_seleccionados_posiciones):
    if posicion_dado in dados_seleccionados_posiciones:
        dados_seleccionados_posiciones.remove(posicion_dado)
    else:
        dados_seleccionados_posiciones.append(posicion_dado)        
    return dados_seleccionados_posiciones
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
