"""
the application module contains the main application class
uses pygame to create window and draw

creator: Mark Jacobsen
"""
import pygame
import cosystem
import helper
import menu


class Application:
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.finished = False
        self.coord_system = cosystem.CoordinateSystem(0, 0, self.window_width, self.window_height)
        self.mouse_click_pos = False
        self.moving_point = None
        self.image = pygame.image.load(r'images/saitama.jpg')
        self.menu = menu.Menu(0, 0, int(self.window_width / 10), self.window_height)
        self.selected_button = self.menu.buttons[0]
        self.selected_button.set_selected(True)

    def draw(self):
        """
        draw everything on screen
        :return: None
        """
        # self.screen.blit(self.image, (100, 100))
        self.coord_system.draw(self.screen)
        self.menu.draw(self.screen)

    def handle_mouse_down(self):
        """
        handles mouse button down event
        :return: None
        """
        self.mouse_click_pos = pygame.mouse.get_pos()
        if self.selected_button:
            self.moving_point = self.coord_system.handle_click(self.selected_button.functionality)

    def handle_mouse_up(self, event):
        """
        handle mouse button up event
        :param event: the exact pygame event that occurred
        :return:
        """
        current_pos = pygame.mouse.get_pos()
        # add new point
        if current_pos == self.mouse_click_pos and event.button == 1:
            # buttons
            selected_button = self.menu.handle_click(current_pos)
            if selected_button:
                if not self.selected_button or not selected_button == self.selected_button:
                    if self.selected_button:
                        self.selected_button.set_selected(False)
                    selected_button.set_selected(True)
                    self.selected_button = selected_button
                else:
                    selected_button.set_selected(False)
                    self.selected_button = None

            # add point
            if not self.moving_point and not selected_button and self.selected_button:
                if self.selected_button.functionality == "add_point":
                    self.coord_system.add_point(current_pos[0], current_pos[1], self.selected_button.ball_color)
        self.mouse_click_pos = False
        self.moving_point = None

    def handle_events(self):
        """
        handles pygame events
        like closing etc.
        :return:
        """
        for event in pygame.event.get():
            # close application
            if event.type == pygame.QUIT:
                self.finished = True
            # mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_down()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_up(event)
            elif event.type == pygame.MOUSEMOTION:
                current_pos = pygame.mouse.get_pos()
                if self.moving_point:
                    self.coord_system.move_point(self.moving_point, current_pos[0], current_pos[1])
                if self.mouse_click_pos and not self.moving_point:
                    self.coord_system.move(self.mouse_click_pos)
            elif event.type == pygame.MOUSEWHEEL:
                self.coord_system.zoom(event.y)

    def run(self):
        # main loop
        while not self.finished:
            # handle events
            self.handle_events()
            # background color
            self.screen.fill(helper.colors["white"])
            # draw
            self.draw()
            # update
            pygame.display.flip()
