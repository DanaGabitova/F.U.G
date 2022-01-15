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