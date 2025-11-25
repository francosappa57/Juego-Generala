import pygame
from pygame_interface.gui import crear_boton, dibujar_boton, boton_clickeado

def menu(pantalla, font, fondo, fondo_rect, COLOR_FONDO):
    jugar = crear_boton("Jugar", 10, 530, 180, 50)
    salon_de_la_fama = crear_boton("Puntajes", 210, 530, 180, 50)
    creditos = crear_boton("Creditos", 410, 530, 180, 50)
    exit = crear_boton("Salir", 610, 530, 180, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"
            if boton_clickeado(event, jugar):
                return "jugar"
            
            if boton_clickeado(event, salon_de_la_fama):
                return "stats"
            
            if boton_clickeado(event, creditos):
                return "creditos"
            
            if boton_clickeado(event, exit):
                return "salir"


        pantalla.fill(COLOR_FONDO)
        pantalla.blit(fondo, fondo_rect)
        pantalla.blit(fondo, (0, 0))

        dibujar_boton(pantalla, jugar, font)
        dibujar_boton(pantalla, salon_de_la_fama, font)
        dibujar_boton(pantalla, creditos, font)
        dibujar_boton(pantalla, exit, font)

        pygame.display.flip()