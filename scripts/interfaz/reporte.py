import pygame

##Función reporte
##Argumentos:
##    informacion: Diccionario que contiene:
##    diccionario: {
##       "nodo": Objeto de clase Nodo
##       "tiempo": Int del tiempo que se demoró el algoritmo
##       "nodos_expandidos": Int con la cantidad de nodos_expandidos
##       "recorrido": Array de arrays. Array de mapas que contienen el recorrido realizado del bombero
##  }
def reporte(informacion):
    #Se definen valores RGB
    BLACK = (0, 0, 0)

    #Se define el ancho y alto de la ventana
    ANCHO = 1280
    ALTO = 720

    #Se inicializa el Background
    SCREEN = pygame.display.set_mode((ANCHO, ALTO))
    BG = pygame.image.load("assets/reporte.png").convert()

    #Separamos las variables de 'informacion'
    nodo = informacion["nodo"]
    tiempo = informacion["tiempo"]
    nodos_expandidos = informacion["nodos_expandidos"]

    #Variables de iniciación de la ventana
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Reporte')

    #Se declara una fuente
    fuente = pygame.font.Font("assets/font.ttf", 72)
    fuente2 = pygame.font.Font("assets/font.ttf", 36)

    #Crea una superficie sobre la cual el texto será renderizado
    #También se renderizan los datos a dar
    titulo = fuente.render('Reporte', True, BLACK)
    costo = fuente2.render('Costo de la solución: ' + str(nodo.costo), True, BLACK)
    profundidad = fuente2.render('Profundidad del árbol: ' + str(nodo.profundidad), True, BLACK)
    tiempo = fuente2.render('Tiempo tomado: ' + str(round(tiempo, 6)) + ' segundos', True, BLACK)
    nodos_expandidos = fuente2.render('Nodos expandidos: ' + str(nodos_expandidos), True, BLACK)
    titulo_ancho = titulo.get_width()

    while True:
        #Llenar la superficie de blanco
        SCREEN.blit(BG, (0, 0))

        #Diuja el texto
        ventana.blit(titulo, ((ANCHO - titulo_ancho) // 2, 50))
        ventana.blit(costo, (20, 200))
        ventana.blit(profundidad, (20, 300))
        ventana.blit(tiempo, (20, 400))
        ventana.blit(nodos_expandidos, (20, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                quit()

        pygame.display.update()


