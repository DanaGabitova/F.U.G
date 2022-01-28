import pygame
import random
import math
from rcc.images import *

class Enemy:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.rect = None

class FlyingEnemy(Enemy):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        self.speed = random.randrange(1, 3)
        self.offset = [random.randrange(-50, 50), random.randrange(-50, 50)]
        self.bullet_cooldown = 0
        self.animation_count = 0 





    
