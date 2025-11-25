import pygame


def crear_boton(texto, x, y, ancho, alto):
    rect = pygame.Rect(x, y, ancho, alto)
    return {"rect": rect, "texto": texto}

def dibujar_boton(pantalla, boton, font):
    mouse_pos = pygame.mouse.get_pos()
    rect = boton["rect"]

    color = (200, 200, 200)

    if rect.collidepoint(mouse_pos):
        color = (170, 170, 170)
    
    pygame.draw.rect(pantalla, color, rect)

    texto = font.render(boton["texto"], True, (0, 0, 0))
    pantalla.blit(texto, texto.get_rect(center=rect.center))

def boton_clickeado(evento, boton):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if boton["rect"].collidepoint(evento.pos):
            return True
    return False
