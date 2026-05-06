import pygame
import math
from pygame.locals import *
import random
import time


class DemoGame:

    def __init__(self, screen_size=(1280, 720)):
        self.screen_size = screen_size
        self.circle_radius = 75
        self.circle_position = (250, 250)
        self.click_position = (-100, -100)

        # Initialize PyGame
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("My First Game")

        # Define a few colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.cnu_blue = (0, 44, 118)

        self.new_game()


    def new_game(self):
        self.score = 0
        self.game_length = 10
        self.start_time = time.time()
        self.new_circle()


    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                self.click_position = pygame.mouse.get_pos()
                deltax = self.click_position[0] - self.circle_position[0]
                deltay = self.click_position[1] - self.circle_position[1]
                click_distance = math.sqrt(deltax**2 + deltay**2)

                if click_distance < self.circle_radius:
                    self.score += 1
                    self.new_circle()
                self.click_position = (-100, -100)
            if event.type == pygame.KEYDOWN:
                self.new_game()



            print(event)



        # Time remaining
        self.time_remaining = (self.start_time + self.game_length) - time.time()

        if self.time_remaining > 0 :
            self.screen.fill(self.white)
            pygame.draw.circle(self.screen, self.cnu_blue, self.circle_position, self.circle_radius)
            # Create a score string and display it
            score_string = f"Time: {self.time_remaining:.01f} Score: {self.score:2}"
            screen_position = (self.screen_size[0]*.4, self.screen_size[1]*0.)
            rendered_score = pygame.font.SysFont("avenir", 48).render(score_string, True, self.black)
            self.screen.blit(rendered_score, screen_position)
        else:
            self.circle_position = (-100, -100)
            self.screen.fill(self.white)
            screen_position = (self.screen_size[0] * .3, self.screen_size[1] * 0.5)
            rendered_score = pygame.font.SysFont("avenir", 48).render("GAME OVER", True, self.black)
            self.screen.blit(rendered_score, screen_position)

            score_string = f"Time: {0.0:.01f} Score: {self.score:2}"
            screen_position = (self.screen_size[0] * .4, self.screen_size[1] * 0.)
            rendered_score = pygame.font.SysFont("avenir", 48).render(score_string, True, self.black)
            self.screen.blit(rendered_score, screen_position)


        pygame.display.update()

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
