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

def render_button(display, text, font, bold, color, position, clicking):  # 
    text = font.render(text, bold, color)
    text_rect = get_text_rect(text)
    text_rect.center = (position[0] + text_rect.width / 2, position[1]
                        + text_rect.height / 2)
    display.blit(text, position)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos = (mouse_x, mouse_y)
    if text_rect.collidepoint(mouse_pos):
        pygame.draw.rect(display, color, text_rect, 1)
        if clicking:
            pass    
 
def calculate_delta_time(dt, prev_time):
    now = time.time()
    dt = now - prev_time
    prev_time = now
    return dt, prev_time

def particle_burst():
    for x in range(1):
        particles.append(Particle(random.randrange(0, 400), -15,
                                  random.randrange(-1, 1), -0.05,
                                  4, (0, 255, 255), 1))

def handle_particles(display, scroll):
    for particle in particles:
        if particle.lifetime > 0:
            particle.draw(display, scroll)
        else:
            particles.remove(particle)        

def render_shadows(display, scroll, shadow_size):
    for i in reversed(range(3)):
        pygame.draw.circle(display, (0, 0, 0, i * 50),
                           (100 - scroll[0] + 16, 100 - scroll[1] + 16),
                           (shadow_size + (i * 10)))

def fill_displays(displays, colors):
    for index, display in enumerate(displays):
        display.fill(colors[index])
        
def animate(image_list, animation_index, time_to_show_image_on_screen):
    if animation_index + 1 >= len(image_list) * time_to_show_image_on_screen:
        animation_index = 0
    animation_index += 1
