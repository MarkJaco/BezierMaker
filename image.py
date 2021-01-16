"""
module contains image class
images will be displayed on the window, can be re-scaled and moved around

creator: Mark Jacobsen
"""
import pygame


class Image:
    def __init__(self, image_path, x, y, width, height):
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.click_x = 0
        self.click_y = 0

    def on_image(self, x, y):
        """
        checks if x, y position is on the image
        :param x: the x pos to check
        :param y: the y pos to check
        :return: boolean accordingly
        """
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True
        return False

    def set_click_position(self):
        """
        safe the current position in case of click
        :return: None
        """
        self.click_x = self.x
        self.click_y = self.y

    def move(self, mouse_click_pos):
        """
        moves the image according to mouse drag
        :param mouse_click_pos: the initial click position of the mouse
        :return: None
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x_difference = mouse_x - mouse_click_pos[0]
        y_difference = mouse_y - mouse_click_pos[1]
        self.x = self.click_x + x_difference
        self.y = self.click_y + y_difference

    def draw(self, screen):
        """
        draws the image on screen
        :param screen: the pygame screen
        :return: None
        """
        screen.blit(self.image, (self.x, self.y))
