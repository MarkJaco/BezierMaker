"""
the application module contains the main application class
uses pygame to create window and draw

creator: Mark Jacobsen
"""
import pygame
import cosystem
import helper


class Application:
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.finished = False
        self.coord_system = cosystem.CoordinateSystem(0, 0, self.window_width, self.window_height)
        self.mouse_click_pos = False

    def draw(self):
        """
        draw everything on screen
        :return: None
        """
        self.coord_system.draw(self.screen)

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
                self.mouse_click_pos = pygame.mouse.get_pos()
                self.coord_system.set_click_point()
            elif event.type == pygame.MOUSEBUTTONUP:
                current_pos = pygame.mouse.get_pos()
                # add new point
                if current_pos == self.mouse_click_pos and event.button == 1:
                    self.coord_system.add_point(current_pos[0], current_pos[1])
                self.mouse_click_pos = False
            elif event.type == pygame.MOUSEMOTION:
                if self.mouse_click_pos:
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
