import pygame
def window():

    pygame.init()

    INIT_STATE = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 2, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [5, 0, 0, 6, 4, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [3, 0, 0, 0, 2, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    ]

    #colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255,0,0)
    GREEN = (0,153,0)
    BLUE = (0,102,255)
    GREY = (96,96,96)
    ORANGE = (250,145,54)

    font = pygame.font.Font(None, 32)

    weight = 600
    height = 600
    screen = pygame.display.set_mode((weight, height))


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
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 1:
                    pygame.draw.rect(screen, GREY, (j*60, i*60, 60, 60))
                elif state[i][j] == 2:
                    pygame.draw.rect(screen, ORANGE, (j*60, i*60, 60, 60))
                elif state[i][j] == 3:
                    pygame.draw.rect(screen, RED, (j*60, i*60, 60, 60))
                    text = font.render("1L",True,BLACK)
                    screen.blit(text,(j*60+20,i*60+20))
                elif state[i][j] == 4:
                    pygame.draw.rect(screen, RED, (j*60, i*60, 60, 60))
                    text = font.render("2L",True,BLACK)
                    screen.blit(text,(j*60+20,i*60+20))
                elif state[i][j] == 5:
                    pygame.draw.rect(screen, GREEN, (j*60, i*60, 60, 60))
                elif state[i][j] == 6:
                    pygame.draw.rect(screen, BLUE, (j*60, i*60, 60, 60))
                elif state[i][j] == 7:
                    pygame.draw.rect(screen, WHITE, (j*60, i*60, 60, 60))
                else:
                    pygame.draw.rect(screen, WHITE, (j*60, i*60, 60, 60))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(WHITE)

        #---draw here---
        print_rects(INIT_STATE)
        draw_grid()
        

        #---end draw---
        pygame.display.flip()