"""
module contains button class
buttons will have the ability to be clicked on and activate different functionality

creator: Mark Jacobsen
"""
import pygame
import helper


class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = helper.colors["grey"]
        self.selected = False
        self.thick = 3
        self.functionality = "None"

    def on_button(self, x, y):
        """
        checks if the given point is on the button
        :param x: the window x coordinate to check
        :param y: the window y coordinate to check
        :return: boolean accordingly
        """
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True
        return False

    def set_selected(self, boolean):
        """
        sets the button to selected or not selected
        :param boolean: True or False should the button be selected
        :return: None
        """
        self.selected = boolean
        if boolean:
            self.color = helper.colors["light_green"]
        else:
            self.color = helper.colors["grey"]

    def draw(self, screen):
        """
        draw the button onto the window
        :param screen: the window to draw on
        :return: None
        """
        # draw main rect
        outer_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, helper.colors["black"], outer_rect, self.thick)
        inner_rect = pygame.Rect(self.x + self.thick, self.y + self.thick, self.width - self.thick * 2,
                                 self.height - self.thick * 2)
        pygame.draw.rect(screen, self.color, inner_rect)


class PointButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.radius = 10
        self.ball_color = helper.colors["red"]
        self.functionality = "add_point"

    def set_ball_color(self, color):
        """
        set new ball color
        :param color: the new color as rgb ()
        :return: None
        """
        self.ball_color = color

    def draw(self, screen):
        """
        draw the button onto the window
        with additional circle
        :param screen: the window to draw on
        :return: None
        """
        # draw rect
        super(PointButton, self).draw(screen)
        # additional circle
        pygame.draw.circle(screen, self.ball_color, (self.x + self.width / 2, self.y + self.height / 2), self.radius)


class DeleteButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.cross_color = helper.colors["red"]
        self.cross_width = 5
        self.functionality = "delete"

    def draw(self, screen):
        """
        draw the button onto the window
        with additional cross
        :param screen: the window to draw on
        :return: None
        """
        # draw rect
        super(DeleteButton, self).draw(screen)
        # draw cross
        start_point = (self.x + self.thick, self.y + self.thick)
        end_point = (self.x + self.width - self.thick, self.y + self.height - self.thick)
        pygame.draw.line(screen, self.cross_color, start_point, end_point, self.cross_width)
        start_point = (self.x + self.thick, self.y + self.height - self.thick)
        end_point = (self.x + self.width - self.thick, self.y + self.thick)
        pygame.draw.line(screen, self.cross_color, start_point, end_point, self.cross_width)


class ExportButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.arrow_color = helper.colors["black"]
        self.functionality = "export"

    def draw(self, screen):
        """
        draw the button onto the window
        with additional arrow
        :param screen: the window to draw on
        :return: None
        """
        # draw rect
        super(ExportButton, self).draw(screen)
        # arrow
        point1 = (self.x + self.width / 5, self.y + self.height / 2)
        point2 = (self.x + self.width / 2, self.y + self.height / 5)
        point3 = (self.x + self.width - self.width / 5, self.y + self.height / 2)
        pygame.draw.polygon(screen, self.arrow_color, (point1, point2, point3))
        start_point = (self.x + self.width / 2, self.y + self.height / 2)
        end_point = (self.x + self.width / 2, self.y + self.height - self.height / 5)
        pygame.draw.line(screen, self.arrow_color, start_point, end_point, 10)
