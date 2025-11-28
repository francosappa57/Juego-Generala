import pygame
import random
from funciones.funciones import tirada, eliminar_jugada
from calculos.calculos import calcular_total, generala, poker, full, escalera, caras
from validaciones.validaciones import validar_puntaje, validar_iniciales_o_vacio
from archivos.arch_csv.archivos_csv import py_ingresa_ganador
from py_config_json.constantes import DADOS, SELECTOR, FONDO_GANAR, FONDO_JUGAR_RAN, MUSICA_JUGAR, MUSICA_GANAR, MUSICA_MENU, VOLUMEN_MUSICA, VOLUMEN_CLICK, VOLUMEN_DADO, SONIDO_DADOS, SONIDO_ELEGIR, SONIDO_ERROR, COLOR_TEXTO_CLARO
from .gui import imp_dados_actuales, imp_puntaje_plantilla, reiniciar_puntaje_plantilla

archivo_juego_csv = "archivos/arch_csv/puntajes.csv"

imagenes_dados = []
for img in DADOS:
    dado = pygame.image.load(img)
    dado = pygame.transform.scale(dado, (100, 100))
    imagenes_dados.append(dado)

elegir = pygame.image.load(SELECTOR)
elegir = pygame.transform.scale(elegir, (100, 100))

fondo_ganador= pygame.image.load(FONDO_GANAR)

img_pika = pygame.image.load(FONDO_JUGAR_RAN[0])
img_bulba = pygame.image.load(FONDO_JUGAR_RAN[1])
img_squi = pygame.image.load(FONDO_JUGAR_RAN[2])
lista_fondo_jugar = [img_pika, img_bulba, img_squi]

clock = pygame.time.Clock()


def fin_del_juego(pantalla, font, total):
    nombre = ""
    seguir = True
    pygame.mixer.music.load(MUSICA_GANAR)
    pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
    pygame.mixer.music.play(-1)
    
    while seguir:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "salir"

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        seguir = False
                
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RETURN:
                        validar = validar_iniciales_o_vacio(nombre)
                        if validar:
                            py_ingresa_ganador(archivo_juego_csv, total, nombre)
                            seguir = False           
                    elif event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        nombre += event.unicode

        puntaje_final = font.render(f"PUNTUACION: {total}", True, (COLOR_TEXTO_CLARO)) 
        pantalla.blit(puntaje_final, (267, 240))
        
        txt_ingreso = font.render("Ingresar 3 iniciales", True, (COLOR_TEXTO_CLARO))
        pantalla.blit(txt_ingreso, (260, 290))

        entrada = font.render(nombre, True, (COLOR_TEXTO_CLARO))
        pantalla.blit(entrada, (380, 330))

        clock.tick(60)
        pygame.display.flip()
    
    pygame.mixer.music.load(MUSICA_MENU)
    pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
    pygame.mixer.music.play(-1)    
    return "menu"
    

def py_jugar(pantalla, font):
    #config
    pygame.mixer.music.load(MUSICA_JUGAR)
    pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
    pygame.mixer.music.play(-1)


    clikeo_tirar = pygame.mixer.Sound(SONIDO_ELEGIR)
    clikeo_tirar.set_volume(VOLUMEN_CLICK)

    clikeo_error = pygame.mixer.Sound(SONIDO_ERROR)
    clikeo_error.set_volume(VOLUMEN_CLICK)


    click_dados = []
    for sound in SONIDO_DADOS:
        click = pygame.mixer.Sound(sound)
        click_dados.append(click)

    fondo_random = random.choice(lista_fondo_jugar)

    # inicio de variables
    dados_seleccionados_posiciones = []
    dados_actuales = []
    guardar_jugadas = []
    TOTAL_RONDAS = 2
    VUELTAS_POR_RONDA = 3
    vueltas_restantes = VUELTAS_POR_RONDA
    ronda_actual = 1
    botones_rects = {}
    puntajes_imp = {}
    primero = False
    tiro= False
    
    puntajes = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "escalera": 0, "full": 0, "poker": 0, "generala": 0}

    tirar_dados = pygame.Rect(150, 517, 160, 60)
    
    y_pos = 170
    for i in range(10):
        clave_jugada = str(i+1)
        if i == 0:         
            boton = pygame.Rect(485, y_pos, 120, 45)
        elif i < 6:
            y_pos += 55
            boton = pygame.Rect(485, y_pos, 120, 45)
        elif i == 6:
            y_pos = 170
            boton = pygame.Rect(632, y_pos, 120, 45)
        else:
            y_pos += 55
            boton = pygame.Rect(632, y_pos, 120, 45)
        botones_rects[clave_jugada] = boton
    
    # Inicio de ciclo de pygame
    while True:
        total = calcular_total(puntajes)
        # mouse_pos = pygame.mouse.get_pos()
        
        if primero:
            puntajes["generala"] = 1000
            total = calcular_total(puntajes)
            pantalla.blit(fondo_ganador, (0,0))
            return fin_del_juego(pantalla, font, total)
        
        if ronda_actual > TOTAL_RONDAS:
            pantalla.blit(fondo_ganador, (0,0))
            return fin_del_juego(pantalla, font, total)
            

        if vueltas_restantes < VUELTAS_POR_RONDA and dados_actuales:
            guardar_jugadas = [dados_actuales[i] for i in dados_seleccionados_posiciones]
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.load(MUSICA_MENU)
                pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
                pygame.mixer.music.play(-1)
                return "menu"

            # if tirar_dados.collidepoint(mouse_pos):
            #     color = (170, 170, 170)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if tirar_dados.collidepoint(mx, my):
                    tiro= True
                    if vueltas_restantes == 0:
                        clikeo_error.play()
                    elif vueltas_restantes > 0 and dados_seleccionados_posiciones:
                        clikeo_tirar.play()
                        dados_seleccionados_posiciones = []
                        vueltas_restantes -= 1
                        tirada(guardar_jugadas)
                        dados_actuales = guardar_jugadas
                    else:
                        clikeo_tirar.play()
                        vueltas_restantes -= 1
                        tirada(guardar_jugadas)
                        dados_actuales = guardar_jugadas
                        if len(dados_actuales) == 5 and ronda_actual == 1 and vueltas_restantes == 2:
                            primero = generala(dados_actuales,puntajes)

                if tiro:
                    puntajes_imp = py_planilla(dados_actuales, puntajes)

                for i, dado_rect in enumerate(espacio_dado_lista):
                    if dado_rect.collidepoint(mx,my):
                        dados_seleccionados_posiciones = guardar_dados_py(i, dados_seleccionados_posiciones, click_dados, dados_actuales)
                    
                if vueltas_restantes < 3:
                    for i ,jugada_rect in botones_rects.items():
                        if jugada_rect.collidepoint (mx,my):
                            validar = validar_puntaje(i, puntajes, puntajes_imp)
                            eliminar_jugada(validar, puntajes)
                            if validar:
                                ronda_actual += 1
                                vueltas_restantes = VUELTAS_POR_RONDA
                                dados_actuales = []
                                dados_seleccionados_posiciones = []
                                reiniciar_puntaje_plantilla(puntajes_imp, puntajes)
                                tiro = False
                            else:
                                clikeo_error.play()
                            
        pantalla.blit(fondo_random, (0,0))

        txt_tirar = font.render("TIRAR", True, (COLOR_TEXTO_CLARO))
        txt_tirada = font.render(f"TIRADAS: {vueltas_restantes}/{VUELTAS_POR_RONDA}", True, (COLOR_TEXTO_CLARO))
        
        if ronda_actual > TOTAL_RONDAS:
            txt_ronda = font.render(f"RONDA: {TOTAL_RONDAS}/{TOTAL_RONDAS}", True, (COLOR_TEXTO_CLARO))
        else:    
            txt_ronda = font.render(f"RONDA: {ronda_actual}/{TOTAL_RONDAS}", True, (COLOR_TEXTO_CLARO))
        
        if not primero:
            txt_total = font.render(f"{total}", True, (COLOR_TEXTO_CLARO))
            pantalla.blit(txt_total, (570, 540))
            
        pantalla.blit(txt_tirar, txt_tirar.get_rect(center=tirar_dados.center))
        pantalla.blit(txt_tirada, (143, 463))
        pantalla.blit(txt_ronda, (153, 33))

        espacio_dado_lista = []
        if dados_actuales:
            imp_dados_actuales(dados_actuales, espacio_dado_lista, pantalla, dados_seleccionados_posiciones, imagenes_dados, elegir)
        
        if puntajes_imp:
            imp_puntaje_plantilla(puntajes_imp, puntajes, font, pantalla, botones_rects)

        clock.tick(60)
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


def guardar_dados_py(posicion_dado, dados_seleccionados_posiciones, clicks, dados_actuales):
    if posicion_dado in dados_seleccionados_posiciones:
        dados_seleccionados_posiciones.remove(posicion_dado)
    else:
        for pos, dado in enumerate(dados_actuales):
            if pos == posicion_dado:
                clicks[dado - 1].set_volume(VOLUMEN_DADO)
                clicks[dado - 1].play()
                dados_seleccionados_posiciones.append(posicion_dado)        
    return dados_seleccionados_posiciones
        
    