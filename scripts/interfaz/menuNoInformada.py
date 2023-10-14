import pygame, sys, os
from button import Button
from animacion import animacion

#Adding the partent directory of scripts to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos.amplitud import amplitud

def menuNoInformada():
    #color 
    red = (255,0,0)

    pygame.init()
    W,H = 1280, 720
    SCREEN = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Algoritmo No Informado")

    #music
    pygame.mixer.music.load("audio/fire.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    BG = pygame.image.load("assets/noInformada.png").convert()
    x=0

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/sewer.ttf", size)

    def opcionProfundidad():
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("black")

            PLAY_TEXT = get_font(45).render("window", True, "White")
            pygame.mixer.music.stop()
            animacion() #llamar funcion
            
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)

            pygame.mixer.music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()

            pygame.display.update()
        
    def opcionAmplitud():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")
        
            OPTIONS_TEXT = get_font(45).render("window", True, "Black")

            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            pygame.mixer.music.stop()

            #Se llama a la funcion de amplitud
            informacion = amplitud()
            animacion(informacion) #llamar funcion

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()

            pygame.display.update()

    def opcionCosto():
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("black")

            PLAY_TEXT = get_font(45).render("window", True, "White")
            pygame.mixer.music.stop()
            animacion() #llamar funcion

            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()

            pygame.display.update()

    def main_menu():
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(70).render("ALGORITMO NO INFORMADO", True, "#FFFFFF")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PROFUNDIDAD = Button(image=pygame.image.load("assets/rect.png"), pos=(640, 250), 
                                text_input="PROFUNDIDAD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            AMPLITUD = Button(image=pygame.image.load("assets/rect.png"), pos=(640, 400), 
                                text_input="AMPLITUD", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            COSTOUNIFORME = Button(image=pygame.image.load("assets/rect.png"), pos=(640, 550), 
                                text_input="COSTO", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PROFUNDIDAD, AMPLITUD, COSTOUNIFORME]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PROFUNDIDAD.checkForInput(MENU_MOUSE_POS):
                        opcionProfundidad()
                    if AMPLITUD.checkForInput(MENU_MOUSE_POS):
                        opcionAmplitud()
                    if COSTOUNIFORME.checkForInput(MENU_MOUSE_POS):
                        opcionCosto() 

            pygame.display.update()

    main_menu()