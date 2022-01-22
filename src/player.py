import pygame
from src.font import *
from src.images import *
from src.maps import *

class Player:
    def __init__(self, x, y, movement_speed):
        self.x = x
        self.y = y
        self.player_rect = pygame.Rect(self.x, self.y, 10, 16)