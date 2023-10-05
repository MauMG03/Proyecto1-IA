import pygame
import sys

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Reporte')
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()