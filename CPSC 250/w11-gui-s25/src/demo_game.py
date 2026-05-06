import pygame
import math
from pygame.locals import *
import random


class DemoGame:

    def __init__(self, screen_size=(1280, 720)):
        self.screen_size = screen_size
        self.circle_radius = 75
        self.circle_position = (250, 250)
        pass

    def loop(self):
        pass

    def new_circle(self):
        #Randomly generate circle position and radius
        self.circle_position = random.random()*self.screen_size[0], random.random()*self.screen_size[1]
        self.circle_radius = random.randint(1, 75)

    def run(self):
        while True:
            self.loop()


if __name__ == '__main__':
    game = DemoGame((800, 600))
    game.run()
