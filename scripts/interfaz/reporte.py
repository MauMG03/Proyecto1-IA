import pygame
import sys

def reporte(informacion):
    #Se definen valores RGB
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #Se define el ancho y alto de la ventana
    ANCHO = 1280
    ALTO = 720

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
    titulo = fuente.render('Reporte', True, BLACK, WHITE)
    costo = fuente2.render('Costo de la solución: ' + str(nodo.costo), True, BLACK, WHITE)
    profundidad = fuente2.render('Profundidad del árbol: ' + str(nodo.profundidad), True, BLACK, WHITE)
    tiempo = fuente2.render('Tiempo tomado: ' + str(round(tiempo, 6)) + ' segundos', True, BLACK, WHITE)
    nodos_expandidos = fuente2.render('Nodos expandidos: ' + str(nodos_expandidos), True, BLACK, WHITE)
    titulo_ancho = titulo.get_width()

    while True:
        #Llenar la superficie de blanco
        ventana.fill(WHITE)

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


