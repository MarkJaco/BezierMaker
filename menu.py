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
        needed_buttons = 12
        additional_y = int(self.height / needed_buttons)
        button1 = button.PointButton(0, 0, self.width, additional_y)
        button2 = button.PointButton(0, additional_y, self.width, additional_y)
        button2.set_ball_color(helper.colors["green"])
        button3 = button.PointButton(0, additional_y * 2, self.width, additional_y)
        button3.set_ball_color(helper.colors["purple"])
        button4 = button.PointButton(0, additional_y * 3, self.width, additional_y)
        button4.set_ball_color(helper.colors["orange"])
        button5 = button.PointButton(0, additional_y * 4, self.width, additional_y)
        button5.set_ball_color(helper.colors["blue"])
        button6 = button.PointButton(0, additional_y * 5, self.width, additional_y)
        button6.set_ball_color(helper.colors["black"])
        button7 = button.PointButton(0, additional_y * 6, self.width, additional_y)
        button7.set_ball_color(helper.colors["aquamarine"])
        button8 = button.PointButton(0, additional_y * 7, self.width, additional_y)
        button8.set_ball_color(helper.colors["light_blue"])
        button9 = button.PointButton(0, additional_y * 8, self.width, additional_y)
        button9.set_ball_color(helper.colors["light_green"])
        button10 = button.DeleteButton(0, additional_y * 9, self.width, additional_y)
        button11 = button.UploadButton(0, additional_y * 10, self.width, additional_y)
        button12 = button.ExportButton(0, additional_y * 11, self.width, additional_y)
        return [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
                button12]

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
