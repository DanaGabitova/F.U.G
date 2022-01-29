import pygame
import math
import random
import time
import numpy as np
from rcc.maps import *
from rcc.images import *

pygame.font.init()
particles = []
entities = []


def load_map(map_name):
    blocks = []
    with open(map_name, 'r') as a_file:
        for line in a_file:
            stripped_line = line.strip()
            stripped_line = stripped_line.split(' ')
            blocks.append(stripped_line)
        a_file.close()
        
    lights = []
    gold = []
    enemies = []
    for i in blocks:
        if i[2] == "block14":
            lights.append([int(i[0]), int(i[1]) - 350])
        if i[2] == "block15":
            enemies.append([int(i[0]), int(i[1]) - 350])
            blocks.remove(i)
        if i[2] == "block0":
            gold.append([int(i[0]), int(i[1]) - 350])
            blocks.remove(i)
    return blocks, lights, gold, enemies    

def load_font(font_name, font_size):  # для загрузки шрифта
    return pygame.font.Font(font_name, font_size)

def get_text_rect(text):  
    return text.get_rect()

def render_text(display, text, font, bold, color, position):  # отображение текста
    text = font.render(text, bold, color)
    display.blit(text, position)
