import sys, pygame
import numpy as np
class treat:
    size = width, height = 400, 600
    screen = pygame.display.set_mode(size)
    ## direct Pipe Parameters

    # top = 0
    # bottom = 0
    w = 80
    speed = 2

    def __init__(self):
        self.x = self.width+np.random.randint(0,400)  # x position of pipe
        self.y = self.height / 2 +np.random.randint(0,50)

    def show(self):  # draws two rectangles one top one bot
        pygame.draw.circle(self.screen,(255,255,0),[int(self.x), int(self.y)],13)


    def update(self):
        self.x -= self.speed
