import pygame

class Particle:
    def __init__(self, x, y, x_vel, y_vel, radius, color, gravity_scale):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.gravity = 1
        self.radius = radius
        self.color = color
        self.lifetime = 2000
        self.gravity_scale = gravity_scale

