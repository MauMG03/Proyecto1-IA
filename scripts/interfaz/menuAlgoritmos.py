import pygame, sys
from button import Button
from menuNoInformada import menuNoInformada
from menuInformada import menuInformada


def menuAlgoritmos():

    pygame.init()
    W,H = 1280, 720
    SCREEN = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Algoritmos")

    #music
    pygame.mixer.music.load("../../audio/fire.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    BG = pygame.image.load("../../assets/algoritmos.png").convert()
    x=0

    def get_font(size): 
        return pygame.font.Font("../../assets/Potential Bold.ttf", size)

    def play():
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("black")

            PLAY_TEXT = get_font(45).render("window", True, "White")
            menuNoInformada()

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
        
    def options():
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
            menuInformada()
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)

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

            MENU_TEXT = get_font(100).render("ALGORITMOS", True, "#FFFFFF")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            NOINFORMADA = Button(image=pygame.image.load("../../assets/rect.png"), pos=(640, 250), 
                                text_input="noInformada", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
            INFORMADA = Button(image=pygame.image.load("../../assets/rect.png"), pos=(640, 400), 
                                text_input="Informada", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("../../assets/rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [NOINFORMADA, INFORMADA, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NOINFORMADA.checkForInput(MENU_MOUSE_POS):
                        play()
                    if INFORMADA.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    main_menu()