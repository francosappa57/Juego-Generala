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
    clock.tick(60)
    pantalla.fill((0,0,0))
    pantalla.blit(fondo, (0,0))

    puntajes = cargar_estadisticas(archivo_juego_csv)
    x_pos= 320
    y_pos= 50
    if puntajes == []:
        pantalla.blit(font.render(f"No hay puntajes guardados", True, (150, 0, 0)), (400, 300))
    else:
        for j in range(len(puntajes) - 1):
            for x in range(len(puntajes) - j - 1):
                if int(puntajes[x]["high score"]) < int(puntajes[x + 1]["high score"]):
                    puntajes[x], puntajes[x + 1] = puntajes[x + 1], puntajes[x]       

    for i, puntos in enumerate(puntajes):
        y_pos += 40
        if i == 9:
            pantalla.blit(font.render(f"{i+1}  -" , True, (0, 0, 0)), (220, y_pos))
            pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (0, 0, 0)), (x_pos, y_pos))
            pantalla.blit(font.render(f" {puntos["high score"]}" , True, (0, 0, 0)), (500, y_pos))
            break

        elif i+1 == 1:
            pantalla.blit(font.render(f"{i+1}  -" , True, (255, 215, 0)), (220, y_pos))
            pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (255, 215, 0)), (x_pos, y_pos))
            pantalla.blit(font.render(f" {puntos["high score"]}" , True, (255, 215, 0)), (500, y_pos))
        elif i+1 == 2:
            pantalla.blit(font.render(f"{i+1}  -" , True, (192, 192, 192)), (220, y_pos))
            pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (192, 192, 192)), (x_pos, y_pos))
            pantalla.blit(font.render(f" {puntos["high score"]}" , True, (192, 192, 192)), (500, y_pos))
        elif i+1 == 3:
            pantalla.blit(font.render(f"{i+1}  -" , True, (255, 165, 0)), (220, y_pos))
            pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (255, 165, 0)), (x_pos, y_pos))
            pantalla.blit(font.render(f" {puntos["high score"]}" , True, (255, 165, 0)), (500, y_pos))
        else:      
            pantalla.blit(font.render(f"{i+1}  -" , True, (0, 0, 0)), (220, y_pos))      
            pantalla.blit(font.render(f"{puntos["nombre"]}" , True, (0, 0, 0)), (x_pos, y_pos))
            pantalla.blit(font.render(f" {puntos["high score"]}" , True, (0, 0, 0)), (500, y_pos))
