"""
module contains coordinate system class
the coordinate system class represents a normal mathematical coordinate system

creator: Mark Jacobsen
"""
import pygame
import axis
import helper


class CoordinateSystem:
    def __init__(self, x, y, width, height):
        """
        constructor
        :param x: the x position top left
        :param y: y position top left
        :param width: width of coordinate system
        :param height: height of coordinate system
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outer_border = 5
        self.axis_extra_width = self.width * 5
        self.axis_extra_height = self.height * 5
        self.x_axis = self.create_x_axis()
        self.y_axis = self.create_y_axis()

    def create_x_axis(self):
        """
        makes x axis with correct position
        :return: axis.Axis object
        """
        start_point = [self.x - self.axis_extra_width, self.y + (self.height / 2)]
        end_point = [self.x + self.width + self.axis_extra_width, self.y + (self.height / 2)]
        return axis.Axis(start_point, end_point)

    def create_y_axis(self):
        """
        makes y axis with correct position
        :return: axis.Axis object
        """
        start_point = [self.x + (self.width / 2), self.y - self.axis_extra_height]
        end_point = [self.x + (self.width / 2), self.y + self.height + self.axis_extra_height]
        return axis.Axis(start_point, end_point)

    def set_click_point(self):
        """
        save the points when mouse is dragged for future reference
        :return: None
        """
        self.x_axis.set_click_point()
        self.y_axis.set_click_point()

    def move(self, mouse_click_pos):
        """
        moves the coordinate system according to mouse moving
        :param mouse_click_pos: position where the mouse was initially clicked
        :return: None
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x_difference = mouse_x - mouse_click_pos[0]
        y_difference = mouse_y - mouse_click_pos[1]
        self.x_axis.move(x_difference, y_difference)
        self.y_axis.move(x_difference, y_difference)

    def draw(self, screen):
        """
        draws the coordinate system on the pygame window
        :param screen: the window to draw on
        :return: None
        """
        # outer rectangle
        outer_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, helper.colors["black"], outer_rect, self.outer_border)
        # main axes
        self.x_axis.draw(screen)
        self.y_axis.draw(screen)
        # other lines
        # TODO
