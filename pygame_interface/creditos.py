import pygame
from py_config_json.constantes import FONDO_CREDITOS, MUSICA_CREDITOS, MUSICA_MENU, VOLUMEN_MUSICA

fondo = pygame.image.load(FONDO_CREDITOS)
fondo = pygame.transform.scale(fondo, (800, 600))

clock = pygame.time.Clock()

def py_creditos(pantalla, font):
    #config
    pygame.mixer.music.load(MUSICA_CREDITOS)
    pygame.mixer.music.set_volume(VOLUMEN_MUSICA)
    pygame.mixer.music.play(-1)
    
    pantalla.blit(fondo, (0,0))

    pantalla.blit(font.render(f"Autor/es: Franco Sappa - Luciano Nicolas Torres Tonkowicz", True, (255, 0, 0)), (10, 100))
    pantalla.blit(font.render(f"Fecha: 4/11", True, (255, 0, 0)), (10, 150))
    pantalla.blit(font.render(f"Materia: programación I", True, (255, 0, 0)), (10, 200))
    pantalla.blit(font.render(f"Docentes: Martín Alejandro García - Verónica Natalia Carbonari", True, (255, 0, 0)), (10, 250))
    pantalla.blit(font.render(f"Carrera: Tecnicatura en programación", True, (255, 0, 0)), (10, 300))
    pantalla.blit(font.render(f"Contacto: sappa57@gmail.com - luciano.torres883@gmail.com", True, (255, 0, 0)), (10, 350))
    
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
            