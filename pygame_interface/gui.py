import pygame
from py_config_json.constantes import COLOR_TEXTO_CLARO, COLOR_TEXTO_OSCURO

def crear_boton(texto, x, y, ancho, alto):
    """
        Crea botones principales del programa
    """
    rect = pygame.Rect(x, y, ancho, alto)
    return {"rect": rect, "texto": texto}

def dibujar_boton(pantalla, boton, font):
    """
        Dibuja los rectangulos en la pantalla en el espacio indicado
    """
    mouse_pos = pygame.mouse.get_pos()
    rect = boton["rect"]

    color = (200, 200, 200)

    if rect.collidepoint(mouse_pos):
        color = (170, 170, 170)
    
    pygame.draw.rect(pantalla, color, rect)

    texto = font.render(boton["texto"], True, COLOR_TEXTO_OSCURO)
    pantalla.blit(texto, texto.get_rect(center=rect.center))

def boton_clickeado(evento, boton, click):
    """
        Validacion de clicks
    """
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if boton["rect"].collidepoint(evento.pos):
            click.play()
            return True
    return False

        
def reiniciar_puntaje_plantilla(puntajes_actuales, puntajes):
    """
        Restablece los valores que no puntuaron al finalizar la ronda.

        Args:
            puntajes_actuales(puntajes_imp): Jugadas disponibles en la tirada actual
            puntajes: Diccionario principal
    """
    for i in puntajes_actuales:
        if int(i) < 7 and puntajes[i] == 0:
            puntajes_actuales[i] = 0
        elif int(i) == 7:
            if puntajes["escalera"] == 0:
                puntajes_actuales[i] = 0
        elif int(i) == 8:
            if puntajes["full"] == 0:
                puntajes_actuales[i] = 0
        elif int(i) == 9:
            if puntajes["poker"] == 0:
                puntajes_actuales[i] = 0
        elif int(i) == 10:
            if puntajes["generala"] == 0:
                puntajes_actuales[i] = 0

def imp_dados_actuales(dados, lista, pantalla, dado_seleccionado, imagenes, elegir):
    """
        Imprime los dados de la tirada actual con sus respectivas posiciones.

        Args:
            dados(dados_actuales): Contiene los dados de la tirada actual
            lista(espacio_dado_lista): Lista vacia que va a contener los espacios de los dados actuales
            dado_seleccionado(dados_seleccionados_posiciones): posicion especifica donde se encuentra el dado a guardar
            imagenes(imagenes_dados): Contiene las imagens de cada dado
            elegir: Carga la imagen del selector
    """
    x_base = 50
    y_base = 150
    sep_horizontal= 120
    sep_vertical= 130

    for i, valor in enumerate(dados):
        img = imagenes[valor - 1]
        if i < 3:
            x_pos = x_base + i * sep_horizontal
            y_pos = y_base
        elif i == 3:
            x_pos = x_base + (i - 2) * sep_horizontal / 2
            y_pos = y_base + sep_vertical
        else:
            x_pos = x_base + (i - 3) * sep_horizontal + 75
            y_pos = y_base + sep_vertical
        espacio_dado = img.get_rect(topleft=(x_pos, y_pos))
        lista.append(espacio_dado)
        pantalla.blit(img, (x_pos, y_pos))

        if i in dado_seleccionado:
            pantalla.blit(elegir, espacio_dado)


def imp_puntaje_plantilla(puntaje_actual, puntajes, font, pantalla, botones):
    """
        Se encarga de mostrar los puntajes de la planilla en tiempo real.

        Args:
            Puntaje_actual(puntajes_imp): Jugadas disponibles en la tirada actual
            Puntajes: Diccionario principal
            Botones(botones_rects): posicion donde se encuentra cada puntaje

    """
    for i in puntaje_actual:
        if int(i) <= 6 and puntajes[i] != 0:
            texto_superficie = font.render(str(puntajes[i]), True, (255,0,0))
        elif int(i) == 7:
            if puntajes["escalera"] != 0:
                texto_superficie = font.render(str(puntajes["escalera"]), True, (255,0,0))
            else:
                if puntaje_actual[i] != 0:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (10,171,0))
                else:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (COLOR_TEXTO_CLARO))
        elif int(i) == 8:
            if puntajes["full"] != 0:
                texto_superficie = font.render(str(puntajes["full"]), True, (255,0,0))
            else:
                if puntaje_actual[i] != 0:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (10,171,0))
                else:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (COLOR_TEXTO_CLARO))
        elif int(i) == 9:
            if puntajes["poker"] != 0:
                texto_superficie = font.render(str(puntajes["poker"]), True, (255,0,0))
            else:
                if puntaje_actual[i] != 0:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (10,171,0))
                else:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (COLOR_TEXTO_CLARO))
        elif int(i) == 10:
            if puntajes["generala"] != 0:
                texto_superficie = font.render(str(puntajes["generala"]), True, (255,0,0))
            else:
                if puntaje_actual[i] != 0:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (10,171,0))
                else:
                    texto_superficie = font.render(str(puntaje_actual[i]), True, (COLOR_TEXTO_CLARO))
        else:
            if puntaje_actual[i] != 0:
                texto_superficie = font.render(str(puntaje_actual[i]), True, (10,171,0))
            else:
                texto_superficie = font.render(str(puntaje_actual[i]), True, (COLOR_TEXTO_CLARO))
        texto_rect = texto_superficie.get_rect(center=botones[i].center) 
        pantalla.blit(texto_superficie, texto_rect)