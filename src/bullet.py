import pygame
import math
import numpy as np
import time


class Bullet:
    def __init__(self, x, y, mouse_x, mouse_y, scroll, image, rot_angle):
        self.x = x
        self.y = y
        self.angle = math.atan2((self.y)-scroll[1]-mouse_y,
                                (self.x)-scroll[0]-mouse_x)
        self.x_vel = math.cos(self.angle)*2
        self.y_vel = math.sin(self.angle)*2
        self.image = image
        self.rot_angle = rot_angle
        self.y_vel = 3
        self.start_time = time.time()
        

