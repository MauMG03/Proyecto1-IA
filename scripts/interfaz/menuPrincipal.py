import pygame, sys
import tkinter as tk
from button import Button
from menuAlgoritmos import menuAlgoritmos
from tkinter import filedialog, messagebox

#color 
red = (255,0,0)

pygame.init()
W,H = 1280, 720
SCREEN = pygame.display.set_mode((W,H))
pygame.display.set_caption("Menu")

#music
pygame.mixer.music.load("../../audio/fire.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
#pygame.mixer.music.stop()


BG = pygame.image.load("../../assets/Background.png").convert()
x=0

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../../assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("window", True, "White")
        menuAlgoritmos()

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
                    menuPrincipal()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(64).render("MEMBERS ", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(650, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        MEMBER1_TEXT = get_font(28).render("Mauricio Muñoz Gutierrez - 2123687", True, "Black")
        MEMBER1_RECT = MEMBER1_TEXT.get_rect(center=(650, 250))
        SCREEN.blit(MEMBER1_TEXT, MEMBER1_RECT)

        MEMBER2_TEXT = get_font(28).render("Juleipssy Daianne Cely Archila - 2122036", True, "Black")
        MEMBER2_RECT = MEMBER2_TEXT.get_rect(center=(650, 350))
        SCREEN.blit(MEMBER2_TEXT, MEMBER2_RECT)

        MEMBER3_TEXT = get_font(28).render("Sebastian Idrobo Avirama - 2122637", True, "Black")
        MEMBER3_RECT = MEMBER1_TEXT.get_rect(center=(650, 450))
        SCREEN.blit(MEMBER3_TEXT, MEMBER3_RECT)
        

        OPTIONS_BACK = Button(image=None, pos=(640, 660), 
                            text_input="BACK", font=get_font(45), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    menuPrincipal()

        pygame.display.update()

def map():
    file = filedialog.askopenfilenames(
        title = "Seleccione el archivo del mundo",
        filetypes=[("Text files", "*.txt")]
    )

    if file:
        with open(file[0], "r") as file:
            #Leer el contenido del archivo
            content = file.read()

        init_state = eval(content)

        BLACK = (0,0,0)
        weight = 600 + 321
        height = 600 + 21
        spacing = 60

        def draw_grid(start_x, start_y):
            for i in range(start_y, height, spacing):
                pygame.draw.line(SCREEN, BLACK, (start_x, i), (weight, i))

            for i in range(start_x, weight, spacing):
                pygame.draw.line(SCREEN, BLACK, (i, start_y), (i, height))


        def print_rects(state, start_x, start_y):
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
                        SCREEN.blit(muro, (j*60+start_x, i*60+start_y))
                    elif state[i][j] == 2:
                        SCREEN.blit(fuego, (j*60+start_x, i*60+start_y))
                    elif state[i][j] == 3:
                        SCREEN.blit(balde1, (j*60+start_x, i*60+start_y))
                    elif state[i][j] == 4:
                        SCREEN.blit(balde2, (j*60+start_x, i*60+start_y))
                    elif state[i][j] == 5:
                        SCREEN.blit(robot, (j*60+start_x, i*60+start_y))
                    elif state[i][j] == 6:
                        SCREEN.blit(agua, (j*60+start_x, i*60+start_y))
                    else:
                        SCREEN.blit(cesped, (j*60+start_x, i*60+start_y))


        while True:
            #Draw white and take the position of the mouse
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.blit(BG, (0, 0))

            print_rects(init_state, 320, 20)
            draw_grid(320,20)

            OPTIONS_BACK = Button(image=pygame.image.load("../../assets/rect.png"), pos=(640, 680), 
                                text_input="BACK", font=get_font(45), base_color="Black", hovering_color="Green")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        menuPrincipal()

            pygame.display.flip()
    else:
        messagebox.showwarning("Error", "No se seleccionó ningún archivo")


def menuPrincipal():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(590, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../../assets/rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("../../assets/rect.png"), pos=(640, 400), 
                            text_input="MEMBERS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MENU_BUTTON = Button(image=pygame.image.load("../../assets/rect.png"), pos=(640, 550), 
                            text_input="VIEW MAP", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, MENU_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    map()

        pygame.display.update()

menuPrincipal()