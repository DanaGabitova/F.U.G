import pygame
import random
import numpy as np

class Entity:
    def __init__(self, x, y, image, alpha, function, vector, color):
        self.x = x
        self.y = y
        self.color = color
        try:
            self.image = image.copy()
        except:
            self.image = None
