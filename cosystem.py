"""
module contains coordinate system class
the coordinate system class represents a normal mathematical coordinate system

creator: Mark Jacobsen
"""
import pygame
import axis
import point
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
        self.line_distance = 100
        self.zoom_amount = 10
        self.max_zoom = 300
        self.min_zoom = 20
        self.x_axis = self.create_x_axis()
        self.y_axis = self.create_y_axis()
        self.horizontal_lines = self.get_horizontal_lines()
        self.vertical_lines = self.get_vertical_lines()
        self.points = [point.Point(1, 1)]
        self.origin = [self.x + (self.width / 2), self.y + (self.height / 2)]
        self.origin_click_point = []
        self.print_errors = False

    def __error(self, message):
        """
        handles errors and prints them
        :param message: the message to print
        :return: None
        """
        if self.print_errors:
            print("An error has occurred here is the message:")
            print(message)

    def create_x_axis(self):
        """
        makes x axis with correct position
        :return: axis.Line object
        """
        start_point = [self.x - self.axis_extra_width, self.y + (self.height / 2)]
        end_point = [self.x + self.width + self.axis_extra_width, self.y + (self.height / 2)]
        x_axis = axis.Line(start_point, end_point)
        x_axis.color = helper.colors["black"]
        return x_axis

    def create_y_axis(self):
        """
        makes y axis with correct position
        :return: axis.Line object
        """
        start_point = [self.x + (self.width / 2), self.y - self.axis_extra_height]
        end_point = [self.x + (self.width / 2), self.y + self.height + self.axis_extra_height]
        y_axis = axis.Line(start_point, end_point)
        y_axis.color = helper.colors["black"]
        return y_axis

    def get_horizontal_lines(self):
        """
        creates all horizontal lines for coordinate system
        :return: list of axis.Line objects
        """
        horizontal_lines = []
        y_coord = int(self.x_axis.start_pos[1])
        # go down
        for y in range(y_coord + self.line_distance, y_coord + self.axis_extra_height, self.line_distance):
            start_point = [self.x - self.axis_extra_height, y]
            end_point = [self.x + self.width + self.axis_extra_height, y]
            line = axis.Line(start_point, end_point)
            horizontal_lines.append(line)
        # go up
        for y in range(y_coord - self.line_distance, y_coord - self.axis_extra_height, -self.line_distance):
            start_point = [self.x - self.axis_extra_height, y]
            end_point = [self.x + self.width + self.axis_extra_height, y]
            line = axis.Line(start_point, end_point)
            horizontal_lines.append(line)
        return horizontal_lines

    def get_vertical_lines(self):
        """
        creates all vertical lines for coordinate system
        :return: list of axis.Line objects
        """
        vertical_lines = []
        x_coord = int(self.y_axis.start_pos[0])
        # go right
        for x in range(x_coord + self.line_distance, x_coord + self.axis_extra_width, self.line_distance):
            start_point = [x, self.y - self.axis_extra_width]
            end_point = [x, self.y + self.height + self.axis_extra_width]
            line = axis.Line(start_point, end_point)
            vertical_lines.append(line)
        # go left
        for x in range(x_coord - self.line_distance, x_coord - self.axis_extra_width, -self.line_distance):
            start_point = [x, self.y - self.axis_extra_width]
            end_point = [x, self.y + self.height + self.axis_extra_width]
            line = axis.Line(start_point, end_point)
            vertical_lines.append(line)
        return vertical_lines

    def zoom(self, direction):
        """
        zooms in or out of the coordinate system
        :param direction: 1 for in -1 for out
        :return: None
        """
        if direction == 1:
            if self.line_distance + self.zoom_amount > self.max_zoom:
                return
            self.line_distance += self.zoom_amount
        elif direction == -1:
            if self.line_distance - self.zoom_amount < self.min_zoom:
                return
            self.line_distance -= self.zoom_amount
        self.horizontal_lines = self.get_horizontal_lines()
        self.vertical_lines = self.get_vertical_lines()

    def set_click_point(self):
        """
        save the points when mouse is dragged for future reference
        :return: None
        """
        self.origin_click_point = self.origin[:]
        self.x_axis.set_click_point()
        self.y_axis.set_click_point()
        for h_line in self.horizontal_lines:
            h_line.set_click_point()
        for v_line in self.vertical_lines:
            v_line.set_click_point()

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
        # move other lines
        for h_line in self.horizontal_lines:
            h_line.move(x_difference, y_difference)
        for v_line in self.vertical_lines:
            v_line.move(x_difference, y_difference)
        # move origin
        self.origin[0] = self.origin_click_point[0] + x_difference
        self.origin[1] = self.origin_click_point[1] + y_difference

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
        for h_line in self.horizontal_lines:
            h_line.draw(screen)
        for v_line in self.vertical_lines:
            v_line.draw(screen)
        # points
        for p in self.points:
            p.draw(screen, self.origin, self.line_distance)

