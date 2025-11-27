import pygame
from archivos.arch_csv.archivos_csv import cargar_estadisticas
archivo_juego_csv = "archivos/arch_csv/puntajes.csv"
fondo = pygame.image.load("assets/UI/LISTA_PUNTAJES2.png")
clock = pygame.time.Clock()


def py_puntaje(pantalla, font):
    #config
    pygame.mixer.music.load("assets/OST/54. Hall Of Fame.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    volver = pygame.Rect(17, 520, 50, 60)
    
    puntajes = cargar_estadisticas(archivo_juego_csv)
    x_pos_signo = 230
    x_pos_nombre = 375
    x_pos_puntaje = 520
    y_pos= 50
    
    pantalla.fill((0,0,0))
    pantalla.blit(fondo, (0,0))
    
    if not puntajes:
        pantalla.blit(font.render(f"No hay puntajes guardados", True, (150, 0, 0)), (230, 300))
    else:
        for j in range(len(puntajes) - 1):
            for x in range(len(puntajes) - j - 1):
                if int(puntajes[x]["high score"]) < int(puntajes[x + 1]["high score"]):
                    puntajes[x], puntajes[x + 1] = puntajes[x + 1], puntajes[x]       

        for i, puntos in enumerate(puntajes):
            y_pos += 40
            if i == 0:
                pantalla.blit(font.render(f"{i+1}  -" , True, (255, 215, 0)), (x_pos_signo, y_pos))
                pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (255, 215, 0)), (x_pos_nombre, y_pos))
                pantalla.blit(font.render(f" {puntos["high score"]}" , True, (255, 215, 0)), (x_pos_puntaje, y_pos))
            elif i == 1:
                pantalla.blit(font.render(f"{i+1}  -" , True, (192, 192, 192)), (x_pos_signo, y_pos))
                pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (192, 192, 192)), (x_pos_nombre, y_pos))
                pantalla.blit(font.render(f" {puntos["high score"]}" , True, (192, 192, 192)), (x_pos_puntaje, y_pos))
            elif i == 2:
                pantalla.blit(font.render(f"{i+1}  -" , True, (255, 165, 0)), (x_pos_signo, y_pos))
                pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (255, 165, 0)), (x_pos_nombre, y_pos))
                pantalla.blit(font.render(f" {puntos["high score"]}" , True, (255, 165, 0)), (x_pos_puntaje, y_pos))
            elif i < 10:
                pantalla.blit(font.render(f"{i+1}  -" , True, (0, 0, 0)), (x_pos_signo, y_pos))
                pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (0, 0, 0)), (x_pos_nombre, y_pos))
                pantalla.blit(font.render(f" {puntos["high score"]}" , True, (0, 0, 0)), (x_pos_puntaje, y_pos))
            
    # pygame.draw.rect(pantalla, (150,0,0), volver)
        
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if volver.collidepoint(mx, my):
                    pygame.mixer.music.load("assets/OST/03. Title Screen.mp3")
                    pygame.mixer.music.set_volume(0.05)
                    pygame.mixer.music.play(-1)
                    return "menu"
        

        


