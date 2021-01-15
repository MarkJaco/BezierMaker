"""
the application module contains the main application class
uses pygame to create window and draw

creator: Mark Jacobsen
"""
import pygame


class Application:
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.finished = False

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
