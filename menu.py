"""
module contains the menu class
the menu contains multiple buttons which activate different functionalities

creator: Mark Jacobsen
"""
import pygame
import button
import helper


class Menu:
    def __init__(self, x, y, width, height):
        """
        constructor
        :param x: left
        :param y: top
        :param width: width
        :param height: height
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = helper.colors["grey"]
        self.buttons = self.get_buttons()

    def get_buttons(self):
        """
        creates the necessary buttons for the menu
        :return: list of button.Button objects
        """
        needed_buttons = 4
        additional_y = int(self.height / needed_buttons)
        button1 = button.PointButton(0, 0, self.width, additional_y)
        button2 = button.PointButton(0, additional_y, self.width, additional_y)
        button2.set_ball_color(helper.colors["orange"])
        button3 = button.DeleteButton(0, additional_y * 2, self.width, additional_y)
        button4 = button.ExportButton(0, additional_y * 3, self.width, additional_y)
        return [button1, button2, button3, button4]

    def handle_click(self, mouse_pos):
        """
        handle mouse click
        :param mouse_pos: the mouse click position
        :return: a button object if it was clicked or None
        """
        for b in self.buttons:
            if b.on_button(mouse_pos[0], mouse_pos[1]):
                return b

    def draw(self, screen):
        """
        draw the menu on the window
        :param screen: the window to draw onto
        :return: None
        """
        # draw main rect
        outer_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        thick = 3
        pygame.draw.rect(screen, helper.colors["black"], outer_rect, thick)
        # draw the buttons
        for b in self.buttons:
            b.draw(screen)
