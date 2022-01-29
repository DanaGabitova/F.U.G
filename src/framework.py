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
