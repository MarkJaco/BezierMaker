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

    def draw(self, screen):
        """
        draws the axis on window
        :param screen: the pygame window to draw on
        :return: None
        """
        pygame.draw.line(screen, helper.colors["black"], self.start_pos, self.end_pos, self.axis_width)