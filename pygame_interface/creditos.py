import pygame
from py_config_json.constantes import FONDO_CREDITOS, MUSICA_CREDITOS, MUSICA_MENU, VOLUMEN_MUSICA, COLOR_TEXTO_OSCURO

fondo = pygame.image.load(FONDO_CREDITOS)
fondo = pygame.transform.scale(fondo, (800, 600))

clock = pygame.time.Clock()

def py_creditos(pantalla, font):
    #config
    pygame.mixer.music.load(MUSICA_CREDITOS)
    pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
    pygame.mixer.music.play(-1)
    centro_pantalla = pantalla.get_rect()
    y_pos = 80
    
    alumnos = font.render(f"Autor/es: Franco Sappa - Luciano Nicolas Torres Tonkowicz", True, COLOR_TEXTO_OSCURO)
    fecha = font.render(f"Fecha: 4/11", True, COLOR_TEXTO_OSCURO)
    materia = font.render(f"Materia: programación I", True, COLOR_TEXTO_OSCURO)
    docentes = font.render(f"Docentes: Martín Alejandro García - Verónica Natalia Carbonari", True, COLOR_TEXTO_OSCURO)
    carrera = font.render(f"Carrera: Tecnicatura en programación", True, COLOR_TEXTO_OSCURO)
    contacto = font.render(f"Contacto: sappa57@gmail.com - luciano.torres883@gmail.com", True, COLOR_TEXTO_OSCURO)
    
    lista_creditos = [alumnos,fecha,materia,docentes,carrera,contacto]
    
    pantalla.blit(fondo, (0,0))
    
    for elmento in lista_creditos:
        centro = elmento.get_rect()
        centro.centerx = centro_pantalla.centerx
        centro.y = y_pos
        pantalla.blit(elmento, centro)
        y_pos += 80
        
    pygame.display.flip()

    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.load(MUSICA_MENU)
                pygame.mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)
                return "menu"       
            