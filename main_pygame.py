import pygame
from pygame_interface.menu import menu
from pygame_interface.jugar import py_jugar
from pygame_interface.puntajes import py_puntaje

ANCHO= 800
ALTO= 600

pygame.init()

#music
pygame.mixer.init()
pygame.mixer.music.load("assets/OST/03. Title Screen.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

#click sounds
click_sound = pygame.mixer.Sound("assets/Cries/25.wav")
# click_sound = pygame.mixer.Sound.set_volume(0.05)

#font
font = pygame.font.Font("assets/Font/5_2.ttf", 30)

pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption("PokeGenerala")
fondo= pygame.image.load("assets/Pikachu_background.png").convert_alpha()
fondo_rect = fondo.get_rect()
r, g, b = 200, 160, 0
COLOR_FONDO = r,g,b
estado_transicion = 0
VELOCIDAD_CAMBIO = 10
reloj = pygame.time.Clock()

ejecutando = True
pantalla_actual = "menu"

while ejecutando:
    reloj.tick(60)

    if pantalla_actual == "menu":
        pantalla_actual = menu(pantalla, font, fondo, fondo_rect, COLOR_FONDO)
    elif pantalla_actual == "jugar":
        pantalla_actual = py_jugar(pantalla, font)
    elif pantalla_actual == "stats":
        pantalla_actual = py_puntaje(pantalla,font)
    elif pantalla_actual == "creditos":
        pass
    elif pantalla_actual == "salir":
            ejecutando = False
    
    # --- Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pantalla_actual = click_sound.play()
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            ejecutando = False

    pygame.display.flip() 

pygame.quit()
