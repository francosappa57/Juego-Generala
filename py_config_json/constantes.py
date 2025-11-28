from py_config_json.datos import cargar_datos

datos = cargar_datos()

TITULO = datos["config"]["ventana"]["titulo"]
ANCHO = datos["config"]["ventana"]["ancho"]
ALTO = datos["config"]["ventana"]["alto"]

FONDO_MENU = datos["config"]["imagen"]["menu"]
# FONDO_JUGAR = datos["config"]["imagen"]["jugar"]
FONDO_JUGAR_RAN = datos["config"]["imagen"]["jugar_ran"]
FONDO_STATS = datos["config"]["imagen"]["stats"]
FONDO_CREDITOS = datos["config"]["imagen"]["creditos"]
FONDO_GANAR = datos["config"]["imagen"]["ganar"]

DADOS = datos["config"]["imagen"]["dados"]
SELECTOR = datos["config"]["imagen"]["selector"]

COLOR_FONDO = datos["config"]["colores"]["fondo"]
COLOR_TEXTO_OSCURO = datos["config"]["colores"]["texto_oscuro"]
COLOR_TEXTO_CLARO = datos["config"]["colores"]["texto_claro"]

MUSICA_MENU = datos["config"]["audio"]["menu"]
MUSICA_JUGAR = datos["config"]["audio"]["jugar"]
MUSICA_STATS = datos["config"]["audio"]["stats"]
MUSICA_CREDITOS = datos["config"]["audio"]["creditos"]
MUSICA_GANAR = datos["config"]["audio"]["ganar"]

SONIDO_DADOS = datos["config"]["audio"]["click"]["dado"]
SONIDO_ELEGIR = datos["config"]["audio"]["click"]["elegir"]
SONIDO_ERROR = datos["config"]["audio"]["click"]["error"]

VOLUMEN_MUSICA = datos["config"]["audio"]["volumen"]["musica"]
VOLUMEN_CLICK = datos["config"]["audio"]["volumen"]["click"]
VOLUMEN_DADO = datos["config"]["audio"]["volumen"]["dado"]

FUENTE_GENERAL = datos["config"]["fuente"]["general"]
SIZE_LETTER_GENERAL = datos["config"]["fuente"]["size"]["general"]
SIZE_LETTER_CREDITOS = datos["config"]["fuente"]["size"]["creditos"]