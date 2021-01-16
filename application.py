"""
the application module contains the main application class
uses pygame to create window and draw

creator: Mark Jacobsen
"""
import pygame
import cosystem
import helper
import menu
import image


class Application:
    def __init__(self, width, height):
        # pygame setup
        self.window_width = width
        self.window_height = height
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.screen = pygame.display.set_mode((width, height))
        self.finished = False
        # other setup
        self.coord_system = cosystem.CoordinateSystem(0, 0, self.window_width, self.window_height)
        self.mouse_click_pos = False
        self.moving_point = None
        self.moving_image = None
        self.menu = menu.Menu(0, 0, int(self.window_width / 10), self.window_height)
        self.selected_button = self.menu.buttons[0]
        self.selected_button.set_selected(True)
        self.image = image.Image(r"images/saitama.jpg", 0, 0, 500, 500)

    def handle_mouse_down(self):
        """
        handles mouse button down event
        :return: None
        """
        self.mouse_click_pos = pygame.mouse.get_pos()
        # buttons
        if self.selected_button:
            self.moving_point = self.coord_system.handle_click(self.selected_button.functionality)
        # image managing
        if self.image:
            # move image alone
            if self.image.on_image(self.mouse_click_pos[0], self.mouse_click_pos[1]):
                self.moving_image = self.image
                self.moving_image.set_click_position()
            # move image along
            if not self.moving_point:
                self.image.set_click_position()

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
                # special case exporting
                if selected_button.functionality == "export":
                    self.coord_system.bezier_curve.export()
                # other buttons
                elif not self.selected_button or not selected_button == self.selected_button:
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
        self.moving_image = None

    def handle_mouse_motion(self, event):
        """
        handle the mouse moving events
        :param event: the exact event
        :return: None
        """
        current_pos = pygame.mouse.get_pos()
        if self.moving_point:
            self.coord_system.move_point(self.moving_point, current_pos[0], current_pos[1])
        elif self.moving_image:
            self.moving_image.move(self.mouse_click_pos)
        elif self.mouse_click_pos and not self.moving_point:
            self.coord_system.move(self.mouse_click_pos)
            self.image.move(self.mouse_click_pos)

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
                self.handle_mouse_motion(event)
            elif event.type == pygame.MOUSEWHEEL:
                self.coord_system.zoom(event.y)
                self.image.zoom(event.y)

    def draw(self):
        """
        draw everything on screen
        :return: None
        """
        self.image.draw(self.screen)
        self.coord_system.draw(self.screen)
        self.menu.draw(self.screen)
        # mouse pos text
        mouse_x, mouse_y = pygame.mouse.get_pos()
        m_x, m_y = self.coord_system.convert_window_position(mouse_x, mouse_y)
        text_surface = self.font.render(f'x: {round(m_x, 2)}, y:{round(m_y, 2)}', False, helper.colors["dark_grey"])
        text_pos = (self.window_width - self.window_width / 6, self.window_height - self.window_height / 17)
        self.screen.blit(text_surface, text_pos)

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
