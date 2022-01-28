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
