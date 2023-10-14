import pygame, sys, os
from button import Button
from animacion import animacion

#Adding the partent directory of scripts to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos.avara import avara
from algoritmos.aEstrella import aEstrella

def menuInformada():

    pygame.init()
    W,H = 1280, 720
    SCREEN = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Algoritmos informados")

    #music
    pygame.mixer.music.load("audio/fire.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    BG = pygame.image.load("assets/Informada.png").convert()

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/ANDALAS.ttf", size)

    def opcionAvara():
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("black")

            PLAY_TEXT = get_font(45).render("window", True, "White")

            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)
            pygame.mixer.music.stop()

            #Se llama a la función de avara
            informacion = avara()
            animacion(informacion)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()

            pygame.display.update()
        
    def opcionAEstrella():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)
            pygame.mixer.music.stop()

            #Se llama a la función de avara
            informacion = aEstrella()
            animacion(informacion)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()

            pygame.display.update()

    def main_menu():
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("ALGORITMO INFORMADO", True, "#FFFFFF")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            AVARA = Button(image=pygame.image.load("assets/rect.png"), pos=(640, 250), 
                                text_input="AVARA", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            A = Button(image=pygame.image.load("assets/rect.png"), pos=(640, 400), 
                                text_input="A*", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)
            
            for button in [AVARA, A, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if AVARA.checkForInput(MENU_MOUSE_POS):
                        opcionAvara()
                    if A.checkForInput(MENU_MOUSE_POS):
                        opcionAEstrella()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    main_menu()