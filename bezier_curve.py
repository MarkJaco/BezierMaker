"""
module contains BezierCurve class
BezierCurve draws a curve according to the given anchor points

creator: Mark Jacobsen
"""
import point
import helper


class BezierCurve:
    def __init__(self):
        self.anchor_points = []
        self.color = helper.colors["blue"]
        self.num_steps = 1000
        self.draw_points = []

    def add_anchor_point(self, anchor_point):
        """
        adds anchor point to the curve
        :param anchor_point: the point to add point.Point object
        :return: None
        """
        self.anchor_points.append(anchor_point)

    def create_curve(self):
        """
        creates the bezier curve
        :return: None
        """
        # check if enough points
        if len(self.anchor_points) < 3:
            return
        # clear previous points
        self.draw_points = []
        # create curve
        n = len(self.anchor_points) - 1
        for t in range(0, self.num_steps, 1):
            t = t / self.num_steps
            draw_point_x = 0
            draw_point_y = 0
            for i, anchor_point in enumerate(self.anchor_points):
                draw_point_x += helper.binomial(n, i) * pow(t, i) * pow(1 - t, n - i) * anchor_point.x
                draw_point_y += helper.binomial(n, i) * pow(t, i) * pow(1 - t, n - i) * anchor_point.y
            new_point = point.Point(draw_point_x, draw_point_y)
            new_point.color = self.color
            self.draw_points.append(new_point)

    def draw(self, screen, origin, line_distance):
        """
        draws the curve as multiple circles
        :param screen: the pygame screen to draw onto
        :param origin: the origin point of the coordinate system
        :param line_distance: the current zoom level
        :return: None
        """
        if len(self.anchor_points) < 3:
            return
        for draw_point in self.draw_points:
            draw_point.draw(screen, origin, line_distance)

