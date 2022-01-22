import pygame
from src.font import *
from src.images import *
from src.maps import *

class Player:
    def __init__(self, x, y, movement_speed):
        self.x = x
        self.y = y
        self.player_rect = pygame.Rect(self.x, self.y, 10, 16)
        self.moving_left = False
        self.moving_right = False
        self.movement_speed = movement_speed
        self.scroll = [0, 0]
        self.vertical_momentum = 0
        self.air_timer = 0
        self.current_animation = 0
        self.animations = [idle_imgs, run_imgs, jump_img]
        self.animation_index = 0
        self.flipped = False
        self.rotation = 0
        self.jumping = False
        self.scale = [18, 27]
