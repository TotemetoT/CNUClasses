"""
    This is the main class for the game.
    It handles the main game loop and the game state.
"""

import math
import random
import time

import pygame
from pygame.locals import *

from src.image_manager import ImageManager
from src.sound_manager import SoundManager


class DuckHunt:
    """Class to manage DuckHunt game."""

    def __init__(self, screensize=(1200, 768)):
        self.verbose = False
        pygame.init()
        self.black, self.white = (0, 0, 0), (255, 255, 255)
        self.screensize = screensize
        self.screenrect = pygame.Rect(0, 0, self.screensize[0], self.screensize[1])
        pygame.display.set_caption("Duck Hunt")
        self.screen = pygame.display.set_mode(self.screensize)
        self.images = ImageManager()
        self.sounds = None
        self.mouse_position = (0, 0)
        self.click_position = (-100, -100)
        self.shells, self.capacity, self.reloading_time = 3, 3, 0
        self.is_reloading, self.is_game_over = False, False
        self.duck_angle = 0
        self.duck_velocity = 0
        self.is_alive = False
        self.new_game()

    def new_game(self):
        """Reinitialize new game."""
        self.score = 0
        self.duck_velocity = 1
        self.duck_angle = 60
        self.is_alive = False
        self.new_duck()
        self.lives = 3
        self.is_game_over = False

    def loop(self):
        """Handle events and draw screen."""
        self.handle_events()

        if self.lives > 0 and not self.is_game_over:
            self.game_over()
        elif not self.is_alive:
            self.new_duck()
        elif not self.is_game_over:
            self.move_duck()
            self.handle_reloading()

        # Uncomment to hide the mouse pointer
        #pygame.mouse.set_visible(False)

        self.screen.blit(pygame.transform.scale(self.images.background, self.screensize), (0, 0))

        self.screen.convert_alpha()
        pygame.display.update()

    def handle_events(self):
        """Process events during loop."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEMOTION:
                self.mouse_position = pygame.mouse.get_pos()
                self.images.sight_rect.center = self.mouse_position
                # Update the sight for target
            elif event.type == MOUSEBUTTONDOWN:
                self.click_position = pygame.mouse.get_pos()
                self.fire()
                print(f" fire at {self.click_position}")
            elif event.type == KEYDOWN:
                # Need to handle reload ('r') and new game (spacebar)
                print(f"key '{pygame.key.name(event.key)}' ({event.key}) {event}")
                if pygame.key.name(event.key) == 'r':
                    self.is_reloading = True
                    self.reloading_time = 20*self.capacity - (20*self.shells)
                elif pygame.key.name(event.key) == 'space' and self.is_game_over:

    def fire(self):
        """
        If shells available fire at duck,
        otherwise play click sound
        """
        if self.shells > 0 and not self.is_reloading:
            self.sounds.blast.play()
            self.shells -= 1
            if self.images.duck_rect.colliderect(self.images.sight_rect):
                self.score += 1
                self.duck_velocity += 1
                self.new_duck()
        else:

    def handle_reloading(self):
        """
        Handle reloading
        """
        if self.is_reloading:
            if self.reloading_time > 0:
                self.reloading_time -= 1
            else:
                self.shells

    def new_duck(self):
        """
        Generate a new duck by setting is_alive,
        a random starting position in x and random angle based on x position
        set y position to 0.66 of screen height.
        Update the duck_rect.center
        """
        self.is_alive = True
        x, y = 0,0
        if random.randint(0,100) % 2 == 0:
            x = int(self.screen[0]*2)
            self.duck_angle = -random.randint(5,35)
        else:
            x = int(self.screensize[0] * .8)
            self.duck_angle = -random.randint(145,175)
        y = int(self.screensize[1]*.66)

        self.images.duck_rect.center = x, y
        if self.verbose:
            print("Duck center:", self.images.duck_rect.center)
    def move_duck(self):
        """
        Update the duck position given velocity and angle
        """
        x = self.images.duck_rect.center[0] + self.duck_velocity*math.cos(math.radians(self.duck_angle))
        y = self.images.duck_rect.center[1] + self.duck_velocity*math.sin(math.radians(self.duck_angle))
        self.images.duck_rect.center = x, y
        if not self.screenrect.colliderect(self.images.duck_rect):
            self.lives -= 1
            if self.lives > 0 and not self.is_game_over:
                self.new_duck()

    def game_over(self):
        """
        Handle game over animation and sound
        """
        if self.verbose:
            print('Game Over!')
        self.is_alive = False
        self.images.duck_rect.center = (-100,-100)
        self.images.dog_rect.center = (self.screensize[0]/2),int(self.screensize[1]/2)
        self.sounds.gameover.play()
    def run(self):
        """Run the loop until exit."""
        while True:
            self.loop()


if __name__ == '__main__':
    game = DuckHunt()
    game.run()
