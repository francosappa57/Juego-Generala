import pygame
from pygame_interface.menu import menu
from pygame_interface.jugar import py_jugar
from pygame_interface.puntajes import py_puntaje
from pygame_interface.creditos import py_creditos
from py_config_json.constantes import ALTO, ANCHO, TITULO, MUSICA_MENU, VOLUMEN_MUSICA, VOLUMEN_CLICK, SONIDO_ELEGIR, FONDO_MENU, FUENTE_GENERAL, SIZE_LETTER_GENERAL, SIZE_LETTER_CREDITOS, COLOR_FONDO

pygame.init()

pygame.display.set_caption(TITULO)

#music
pygame.mixer.init()
pygame.mixer.music.load(MUSICA_MENU)
pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
pygame.mixer.music.play(-1)

#click sounds
click_sound = pygame.mixer.Sound(SONIDO_ELEGIR)
click_sound.set_volume(VOLUMEN_CLICK)

#font
font_general = pygame.font.Font(FUENTE_GENERAL, SIZE_LETTER_GENERAL)
font_creditos = pygame.font.Font(FUENTE_GENERAL, SIZE_LETTER_CREDITOS)

pantalla = pygame.display.set_mode((ANCHO,ALTO))

fondo_menu = pygame.image.load(FONDO_MENU)

reloj = pygame.time.Clock()

ejecutando = True
pantalla_actual = "menu"

while ejecutando:
    if pantalla_actual == "menu":
        pantalla_actual = menu(pantalla, font_general, fondo_menu, COLOR_FONDO, click_sound)
    elif pantalla_actual == "jugar":
        pantalla_actual = py_jugar(pantalla, font_general)
    elif pantalla_actual == "stats":
        pantalla_actual = py_puntaje(pantalla,font_general)
    elif pantalla_actual == "creditos":
        pantalla_actual = py_creditos(pantalla,font_creditos)
    elif pantalla_actual == "salir":
            ejecutando = False


    reloj.tick(60)
    pygame.display.flip() 

pygame.quit()
