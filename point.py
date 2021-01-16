"""
module contains point class
points will be used to draw bezier curves, they serve as ankers
they can be moved around and placed with the mouse

creator: Mark Jacobsen
"""
import pygame
import helper


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = helper.colors["red"]

    def convert_coordinates(self, origin, line_distance):
        """
        converts mathematical coordinates to pygame window coordinates
        :param origin: the origin point of the coordinate system
        :param line_distance: the current zoom level
        :return: [x, y] list of ints
        """
        x_position = origin[0] + (self.x * line_distance)
        y_position = origin[1] - (self.y * line_distance)
        return [x_position, y_position]

    def draw(self, screen, origin, line_distance):
        """
        draws point on the pygame window
        :param screen: the screen to draw on
        :param origin: the origin point of the coordinate system
        :param line_distance: the current zoom level
        :return: None
        """
        draw_coordinates = self.convert_coordinates(origin, line_distance)
        pygame.draw.circle(screen, self.color, draw_coordinates, self.radius)
