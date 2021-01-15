"""
module contains the axis class for the x and the y axis

creator: Mark Jacobsen
"""
import pygame
import helper


class Axis:
    def __init__(self, start_pos, end_pos):
        """
        constructor
        :param start_pos: the start pos of the line
        :param end_pos: the end position of the line
        """
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.axis_width = 3
        self.start_pos_click = [0, 0]
        self.end_pos_click = [0, 0]

    def set_click_point(self):
        """
        save the points when mouse is dragged for future reference
        :return: None
        """
        self.start_pos_click[0] = self.start_pos[0]
        self.start_pos_click[1] = self.start_pos[1]
        self.end_pos_click[0] = self.end_pos[0]
        self.end_pos_click[1] = self.end_pos[1]

    def move(self, x_change, y_change):
        """
        moves the axis according to the new change
        :param x_change: how much to change x pos and where to, as int
        :param y_change: how much to change y pos and where to, as int
        :return: None
        """
        self.start_pos[0] = self.start_pos_click[0] + x_change
        self.end_pos[0] = self.end_pos_click[0] + x_change
        self.start_pos[1] = self.start_pos_click[1] + y_change
        self.end_pos[1] = self.end_pos_click[1] + y_change

    def draw(self, screen):
        """
        draws the axis on window
        :param screen: the pygame window to draw on
        :return: None
        """
        pygame.draw.line(screen, helper.colors["black"], self.start_pos, self.end_pos, self.axis_width)