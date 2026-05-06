import pygame
import math
from pygame.locals import *
import random


class DemoGame:

    def __init__(self, screen_size=(1280, 720)):
        self.screen_size = screen_size
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("My first game")

        self.circle_position = (250, 250)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.cnu_blue = (0,44,118)
        self.score = 0
        self.click_position = (-100,-100)
        self.circle_radius = 75

    def loop(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                self.click_position = pygame.mouse.get_pos()
                deltax = self.click_position[0] - self.click_position[0]
                deltay = self.click_position[1] - self.circle_position[1]
                click_distance = math.sqrt(deltax**2 + deltay**2)
                if click_distance < self.circle_radius:
                    self.score += 1
                    self.click_position = (-100,-100)
                    self.new_circle()

            print(event)
            self.screen.fill(self.white)
            pygame.draw.circle(self.screen, self.cnu_blue, self.circle_position, self.circle_radius)

    def new_circle(self):
        #Randomly generate circle position and radius
        self.circle_position = (random.random()*self.screen_size[0],
                                random.random()*self.screen_size[1])
        self.circle_radius = random.randint(10, 75)  # Make min smaller later

    def run(self):
        while True:
            self.loop()


if __name__ == '__main__':
    game = DemoGame((800, 600))
    game.run()
