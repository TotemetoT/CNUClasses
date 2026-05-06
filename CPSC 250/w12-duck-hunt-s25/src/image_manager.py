"""Manage images in game."""

import pygame


class ImageManager:
    """Manage images in game."""

    def __init__(self):
        self.load_images()

    def load_images(self):
        """Load selected images and set bounding rectangles."""
        self.background = pygame.image.load("images/background.png")
        self.sight = pygame.image.load("images/sight.gif")
        self.dog = pygame.image.load("images/dog.gif")
        self.duck = pygame.image.load("images/greenduck.gif")

        # Optimize images for faster drawing
        self.background.convert()
        self.sight.convert()
        self.dog.convert()
        self.duck.convert()

        self.duck_rect = self.duck.get_rect()
        self.sight_rect = self.sight.get_rect()
        self.dog_rect = self.dog.get_rect()

    def __str__(self):
        """Return string."""
        return "Instance manages images in duck hunt game."
