import pygame
from pygame_interface.menu import menu
from pygame_interface.jugar import py_jugar

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
#font
font = pygame.font.Font(None, 45)

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
    pygame.display.flip() 
    if pantalla_actual == "menu":
        pantalla_actual = menu(pantalla, font, fondo, fondo_rect, COLOR_FONDO)
    elif pantalla_actual == "jugar":
        pantalla_actual = py_jugar(pantalla, font)


    # --- Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False


#    pantalla.fill(COLOR_FONDO)
#    pantalla.blit(fondo, fondo_rect)


 #   pantalla.fill(COLOR_FONDO)
 #   pantalla.blit(fondo, fondo_rect)
pygame.quit()
