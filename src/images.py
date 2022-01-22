import pygame
import os

def load_img(img, transparent):
    if transparent == False:
        image = pygame.image.load(img).convert()
        image.set_colorkey(255, 255, 255)
    else:
        image = pygame.image.load(img)
    return image

test_block = load_img("rcc/images/block0.png", False)

idle_imgs = [load_img("rcc/images/player/idle/idle_1.png", False),
load_img("rcc/images/player/idle/idle_2.png", False),
load_img("rcc/images/player/idle/idle_3.png", False)]

run_imgs = [load_img("rcc/images/player/run/run_1.png", False),
load_img("rcc/images/player/run/run_2.png", False),
load_img("rcc/images/player/run/run_3.png", False),
load_img("rcc/images/player/run/run_4.png", False)]

jump_img = [load_img("rcc/images/player/jump/jump.png", False)]
print(os.path.join('rcc', 'images', 'BottomCornerLeft.png'))
block1 = load_img('rcc/images/BottomCornerLeft.png', False)
block2 = load_img('rcc/images/BottomCornerRight.png', False)
block3 = load_img('rcc/images/Center.png', False)
block4 = load_img('rcc/images/MiddleBottom.png', False)
block5 = load_img('rcc/images/MiddleRowLeft.png', False)
block6 = load_img('rcc/images/MiddleRowRight.png', False)
block7 = load_img('rcc/images/TopCornerLeft.png', False)
block8 = load_img('rcc/images/TopCornerRight.png', False)
block9 = load_img('rcc/images/TopMiddle.png', False)

block10 = load_img('rcc/images/Connecter.png', False)
block11 = load_img('rcc/images/Connecter2.png', False)
block12 =load_img('rcc/images/Connecter3.png', False)
block13 = load_img('rcc/images/Connecter4.png', False)

torch_img = load_img("rcc/images/torch.png", False)

gold_img = load_img("rcc/images/block0.png", False)

bow_img = load_img("rcc/images/Bow.png", False)
arrow_img = load_img("rcc/images/Arrow.png", False)
bomb_img = load_img("rcc/images/Bomb.png", False)
gold_img = load_img("rcc/images/Gold.png", False)

mice_imgs = [load_img("rcc/images/mice/radioactivemice1.png", True),
load_img("rcc/images/mice/radioactivemice2.png", True),
load_img("rcc/images/mice/radioactivemice3.png", True)]
