import pygame, sys
from button import Button

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

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill('black')


        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True,
                                        "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(600, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75),
                           base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    MUSIC_PAUSE = not MUSIC_PAUSE
                    if MUSIC_PAUSE:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    main_menu()

        pygame.display.update()
