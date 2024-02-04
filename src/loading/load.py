from os import read
from os import path
import pygame
from pygame import *


WIDTH = 1204
HEIGHT = 768
FPS = 60

pygame.mixer.pre_init(44100, -16, 1, 512) 
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tomb Of The Mask")
clock = pygame.time.Clock()
# colors
DARK_GRAY = (96, 96 ,96)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0 ,0)
BLUE = (0, 0, 255)
YELLOW = (255,255,25)
PURPLE = (17,76,150)

# Animation:
win_block_sheet = []
win_block_sheet.append(pygame.image.load("1.png").convert())
win_block_sheet.append(pygame.image.load("2.png").convert())
win_block_sheet.append(pygame.image.load("3.png").convert())
win_block_sheet.append(pygame.image.load("4.png").convert())
win_block_sheet.append(pygame.image.load("5.png").convert())
win_block_sheet.append(pygame.image.load("6.png").convert())
win_block_sheet.append(pygame.image.load("7.png").convert())
win_block_sheet.append(pygame.image.load("8.png").convert())


all_sprites = pygame.sprite.Group()



class WinBlock(pygame.sprite.Sprite):
    def __init__(self):
        global win_block_sheet
        pygame.sprite.Sprite.__init__(self)
        self.current_animation = 0
        self.image = win_block_sheet[self.current_animation]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.image.set_colorkey(WHITE)
    def update(self):
        self.current_animation += 0.2
        if self.current_animation >= 8 :
            self.current_animation = 0
        self.image = win_block_sheet[int(self.current_animation)]
        self.image.set_colorkey(WHITE)

winblock = WinBlock()
all_sprites.add(winblock)
        



running = True
while running:
    clock.tick(FPS)
    time_now = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
                
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()