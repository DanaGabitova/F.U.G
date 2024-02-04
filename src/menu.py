import pygame, sys
from button import Button
from main import main

pygame.init()

pygame.mixer.music.load('rcc/sound_effects/music.mp3')
pygame.mixer.music.play(-1)

MUSIC_PAUSE = False

SCREEN = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Menu")

BG = pygame.image.load("rcc/images/Background.png")
BG = pygame.transform.scale(BG, (1920, 1080))


def get_font(size):
    return pygame.font.Font("rcc/font/font.ttf", size)

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True,
                                           "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75),
                              base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()  # добавим после размышлений

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#d9f7fe")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button\
            (image=pygame.image.load("rcc/images/Play Rect.png"),
                             pos=(350, 250),
                             text_input="PLAY", font=get_font(75),
                             base_color="#ff4b63", hovering_color="White")
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("rcc/images/Options Rect.png"),
            pos=(350, 400),
            text_input="OPTIONS", font=get_font(75), base_color="#ff4b63",
            hovering_color="White")
        QUIT_BUTTON = Button\
            (image=pygame.image.load("rcc/images/Quit Rect.png"),
                             pos=(350, 550),
                             text_input="QUIT", font=get_font(75),
                             base_color="#ff4b63", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                    return
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
 

main_menu()
