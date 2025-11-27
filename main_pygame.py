import pygame
from pygame_interface.menu import menu
from pygame_interface.jugar import py_jugar
from pygame_interface.puntajes import py_puntaje
from pygame_interface.creditos import py_creditos
from py_config_json.constantes import ALTO, ANCHO, TITULO, MUSICA_MENU, VOLUMEN_MUSICA, VOLUMEN_CLICK, SONIDO_ELEGIR, FONDO_MENU

pygame.init()

#music
pygame.mixer.init()
pygame.mixer.music.load(MUSICA_MENU)
pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
pygame.mixer.music.play(-1)

#click sounds
click_sound = pygame.mixer.Sound(SONIDO_ELEGIR)
click_sound.set_volume(VOLUMEN_CLICK)

#font
font = pygame.font.Font("assets/Font/Omega Ruby.otf", 30)

pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption(TITULO)
fondo_menu = pygame.image.load(FONDO_MENU).convert_alpha()
fondo_rect = fondo_menu.get_rect()
r, g, b = 200, 160, 0
COLOR_FONDO = r,g,b
# estado_transicion = 0
# VELOCIDAD_CAMBIO = 10
reloj = pygame.time.Clock()

ejecutando = True
pantalla_actual = "menu"

while ejecutando:
    reloj.tick(60)

    if pantalla_actual == "menu":
        pantalla_actual = menu(pantalla, font, fondo_menu, fondo_rect, COLOR_FONDO, click_sound)
    elif pantalla_actual == "jugar":
        pantalla_actual = py_jugar(pantalla, font)
    elif pantalla_actual == "stats":
        pantalla_actual = py_puntaje(pantalla,font)
    elif pantalla_actual == "creditos":
        pantalla_actual = py_creditos(pantalla,font)
    elif pantalla_actual == "salir":
            ejecutando = False

    pygame.display.flip() 

pygame.quit()
