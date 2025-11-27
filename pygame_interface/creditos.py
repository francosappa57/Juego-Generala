import pygame

fondo = pygame.image.load("assets/UI/fondo pokeball.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))

clock = pygame.time.Clock()

def py_creditos(pantalla, font):
    #config
    pygame.mixer.music.load("assets/OST/43. Mystery Gift.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    pantalla.blit(fondo, (0,0))

    pantalla.blit(font.render(f"Autor/es: Franco Sappa - Luciano Nicolas Torres Tonkowicz", True, (255, 0, 0)), (10, 100))
    pantalla.blit(font.render(f"Fecha: 4/11", True, (255, 0, 0)), (10, 200))
    pantalla.blit(font.render(f"Materia: programación I", True, (255, 0, 0)), (10, 300))
    pantalla.blit(font.render(f"Carrera: Tecnicatura en programación", True, (255, 0, 0)), (10, 400))
    pantalla.blit(font.render(f"Contacto: sappa57@gmail.com - luciano.torres883@gmail.com", True, (255, 0, 0)), (10, 500))
    
    pygame.display.flip()

    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.load("assets/OST/03. Title Screen.mp3")
                pygame.mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)
                return "menu"        
            