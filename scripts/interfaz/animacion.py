import pygame, time
from reporte import reporte

##Función animacion
##Argumentos:
##    informacion: Diccionario que contiene: {
##       "nodo": Objeto de clase Nodo
##       "tiempo": Int del tiempo que se demoró el algoritmo
##       "nodos_expandidos": Int con la cantidad de nodos_expandidos
##       "recorrido": Array de arrays. Array de mapas que contienen el recorrido del bombero
##     }

def animacion(informacion = None):

    pygame.init()

    #Estado inicial
    init_state = []

    #colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255,0,0)
    GREEN = (0,153,0)
    BLUE = (0,102,255)
    GREY = (96,96,96)
    ORANGE = (250,145,54)

    #fuentes
    font = pygame.font.Font(None, 32)

    #dimensiones
    weight = 600
    height = 600
    screen = pygame.display.set_mode((weight, height))

    #Se extrae el recorrido del bombero
    try:
        recorrido = informacion["recorrido"]
    except:
        recorrido = None

    def draw_grid():
        # spacing between each line
        spacing = 60

        # draw horizontal lines
        for i in range(0, height, spacing):
            pygame.draw.line(screen, BLACK, (0, i), (weight, i))

        # draw vertical lines
        for i in range(0, weight, spacing):
            pygame.draw.line(screen, BLACK, (i, 0), (i, height))

    def print_rects(state):
        cesped = pygame.image.load("../../assets/cesped.jpeg")
        muro = pygame.image.load("../../assets/muro.jpeg")
        robot = pygame.image.load("../../assets/robot.jpeg")
        fuego = pygame.image.load("../../assets/fuego.png")
        agua = pygame.image.load("../../assets/hidrante.png")
        balde1 = pygame.image.load("../../assets/balde1L.png")
        balde2 = pygame.image.load("../../assets/balde2L.png")

        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 1:
                    screen.blit(muro,(j*60,i*60))
                elif state[i][j] == 2:
                    screen.blit(fuego,(j*60,i*60))
                elif state[i][j] == 3:
                    screen.blit(balde1,(j*60,i*60))
                elif state[i][j] == 4:
                    screen.blit(balde2,(j*60,i*60))
                elif state[i][j] == 5:
                    screen.blit(robot,(j*60,i*60))
                elif state[i][j] == 6:
                    screen.blit(agua,(j*60,i*60))
                else:
                    screen.blit(cesped,(j*60,i*60))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if (recorrido is not None):
            while(recorrido):
                #Toma el estado en cabeza de recorrido
                init_state = recorrido[0]
                #Elimina el estado en cabeza de recorrido
                recorrido.pop(0)
                #Dibuja el estado
                print_rects(init_state)
                draw_grid()
                pygame.display.flip()
                #Espera unos segundos para dibujar el siguiente estado del bombero
                time.sleep(0.25)

                #Si se trata del último estado, entrar aquí para pasar con el reporte
                if (len(recorrido) == 1):
                    init_state = recorrido[0]
                    recorrido.pop(0)
                    print_rects(init_state)
                    draw_grid()
                    pygame.display.flip()
                    time.sleep(3)
                    #Despliegue del reporte
                    reporte(informacion)
        
        #---end draw---
        pygame.display.flip()