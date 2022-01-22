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
        
    def get_input(self, dt): 
        self.player_movement = [0, 0] 
        self.air_timer += 1 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a]: 
            if self.air_timer < 6: 
                self.current_animation = 1 
            else: 
                self.animation_count = 2 
            self.player_movement[0] -= self.movement_speed * dt * 60 
        if keys[pygame.K_d]: 
            if self.air_timer < 6: 
                self.current_animation = 1 
            else: 
                self.animation_count = 2 
            self.player_movement[0] += self.movement_speed * dt * 60 
 
        if not keys[pygame.K_d] and not keys[pygame.K_a]: 
            if self.air_timer < 6: 
                self.current_animation = 0 
            else: 
                self.current_animation = 2 
 
        if self.player_movement[0] > 0: 
            self.flipped = False 
        elif self.player_movement[0] < 0: 
            self.flipped = True 
 
        self.player_movement[1] += self.vertical_momentum 
        self.vertical_momentum += 0.5 
        if self.vertical_momentum > 3: 
            self.vertical_momentum = 3 
