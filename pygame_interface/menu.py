import pygame
from pygame_interface.gui import crear_boton, dibujar_boton, boton_clickeado

clock = pygame.time.Clock()

def menu(pantalla, font, fondo, color_fondo, click):
    """
        Menu principal del juego

    """
    jugar = crear_boton("Jugar", 10, 530, 180, 50)
    salon_de_la_fama = crear_boton("Puntajes", 210, 530, 180, 50)
    creditos = crear_boton("Creditos", 410, 530, 180, 50)
    exit = crear_boton("Salir", 610, 530, 180, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            if boton_clickeado(event, jugar, click):
                return "jugar"
            
            if boton_clickeado(event, salon_de_la_fama, click):
                return "stats"
            
            if boton_clickeado(event, creditos, click):
                return "creditos"
            
            if boton_clickeado(event, exit, click):
                return "salir"


        pantalla.fill(color_fondo)
        pantalla.blit(fondo, (0, 0))

        dibujar_boton(pantalla, jugar, font)
        dibujar_boton(pantalla, salon_de_la_fama, font)
        dibujar_boton(pantalla, creditos, font)
        dibujar_boton(pantalla, exit, font)

        clock.tick(60)
        pygame.display.flip()