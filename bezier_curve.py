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
        self.num_steps = 1000
        self.draw_points = []

    def export(self):
        """
        exports the anchor points
        meaning it prints them in the console
        :return: None
        """
        export_str = ""
        for c, curve in enumerate(self.anchor_points):
            export_str += "bezierKurve" + str(c) + " = {"
            for i, p in enumerate(curve):
                export_str += "{" + str(round(p.x, 3)) + ", " + str(round(p.y, 3)) + "}"
                if not i == len(curve) - 1:
                    export_str += ", "
            export_str += "}\n"
        print(export_str)

    def add_anchor_point(self, anchor_point):
        """
        adds anchor point to the curve
        :param anchor_point: the point to add point.Point object
        :return: None
        """
        if not self.anchor_points:
            self.anchor_points.append([anchor_point])
        else:
            found = False
            for curve in self.anchor_points:
                if curve:
                    if anchor_point.color == curve[0].color:
                        curve.append(anchor_point)
                        found = True
            if not found:
                self.anchor_points.append([anchor_point])
        self.create_curve()

    def remove_anchor_point(self, anchor_point):
        """
        remove given anchor point
        :param anchor_point: the point to remove from list
        :return: None
        """
        for curve in self.anchor_points:
            if curve:
                if curve[0].color == anchor_point.color:
                    curve.remove(anchor_point)
        self.create_curve()

    def create_curve(self):
        """
        creates the bezier curve
        :return: None
        """
        # clear previous points
        self.draw_points = []
        for curve_points in self.anchor_points:
            # check if enough points
            if len(curve_points) < 3:
                continue
            # create curve
            n = len(curve_points) - 1
            for t in range(0, self.num_steps, 1):
                t = t / self.num_steps
                draw_point_x = 0
                draw_point_y = 0
                for i, anchor_point in enumerate(curve_points):
                    draw_point_x += helper.binomial(n, i) * pow(t, i) * pow(1 - t, n - i) * anchor_point.x
                    draw_point_y += helper.binomial(n, i) * pow(t, i) * pow(1 - t, n - i) * anchor_point.y
                new_point = point.Point(draw_point_x, draw_point_y)
                new_point.color = curve_points[0].color
                self.draw_points.append(new_point)

    def draw(self, screen, origin, line_distance):
        """
        draws the curve as multiple circles
        :param screen: the pygame screen to draw onto
        :param origin: the origin point of the coordinate system
        :param line_distance: the current zoom level
        :return: None
        """
        for draw_point in self.draw_points:
            draw_point.draw(screen, origin, line_distance)
