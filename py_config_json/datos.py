import json
import os

configuracion_default = {
    "config": {
        "ventana": {"ancho": 800, "alto": 600, "titulo": "PokeGenerala"},
        
        "audio": {"volumen": {"musica": 0.05, "click": 0.5, "dado": 0.3},
                  "click": {"dado": ["assets/Cries/1.wav","assets/Cries/4.wav","assets/Cries/7.wav","assets/Cries/25.wav","assets/Cries/34.wav","assets/Cries/257.wav"], "elegir": "assets/Sounds/firered_0005.wav", "error": "assets/Sounds/firered_0007.wav"},
                  "menu": "assets/OST/03. Title Screen.mp3",
                  "jugar": "assets/OST/1-49. Game Corner.mp3",
                  "stats": "assets/OST/54. Hall Of Fame.mp3",
                  "creditos": "assets/OST/43. Mystery Gift.mp3",
                  "ganar": "assets/OST/10. Victory! (Trainer).mp3"},
        
        "colores": {"fondo": (200,160,0), "texto_claro": (255,255,255), "texto_oscuro": (0,0,0)},
        
        "imagen": {"dados": ["assets/UI/Dices/Bulbasaur_1.png","assets/UI/Dices/Charmander_2.png","assets/UI/Dices/Squirtle_3.png","assets/UI/Dices/Pikachu_4.png","assets/UI/Dices/Nidoking_5.png","assets/UI/Dices/Blaziken_6.png"],
                   "selector": "assets/UI/Dices/Selector2.png",
                   "menu": "assets/UI/Pikachu_background.png",
                   "jugar_ran": ["assets/UI/Menu_jugar_bulbasaur.png","assets/UI/Menu_jugar_charmander.png","assets/UI/Menu_jugar_squirtle.png","assets/UI/Menu_jugar_pikachu2.png","assets/UI/Menu_jugar_nidoking.png","assets/UI/Menu_jugar_blaziken2.png"],
                   "stats": "assets/UI/ranking.png",
                   "creditos": "assets/UI/paisaje_creditos.jpg",
                   "ganar": "assets/UI/ganaste5.png",
                   "ganar_ran": ["assets/UI/fondo_bulbasaur.jpeg","assets/UI/fondo_charmander.jpeg","assets/UI/fondo_squirtle.jpeg","assets/UI/fondo_pikachu.jpeg","assets/UI/fondo_nidoking.jpeg","assets/UI/fondo_blaiziken.jpeg"]
                   },
        
        "fuente": {"general": "assets/Font/ANDYB.TTF",
                   "size": {"general": 30, "creditos": 30}}
    }   
}

archi_config = "py_config_json/default.json"

def guardar_datos(datos):
    """
        Guarda datos en archivo Json.

    """
    with open(archi_config, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def cargar_datos():
    """
        Carga datos de archivo Json.

    """
    if not os.path.exists(archi_config) or os.path.getsize(archi_config) == 0:
        guardar_datos(configuracion_default)
        return configuracion_default
    
    if os.path.exists(archi_config) != configuracion_default:
        guardar_datos(configuracion_default)
        return configuracion_default
    
    with open(archi_config, "r") as archivo:
        datos = json.load(archivo)

    if "config" not in datos:
        guardar_datos(configuracion_default)
        return configuracion_default
    
    return datos