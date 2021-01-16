"""
module contains helper methods and variables

creator: Mark Jacobsen
"""
from math import factorial as fac

colors = {"black": (0, 0, 0), "white": (255, 255, 255), "grey": (211, 211, 211), "red": (255, 0, 0),
          "blue": (0, 0, 255), "orange": (255, 165, 0), "green": (0, 255, 0), "light_green": (144, 238, 144),
          "purple": (255, 0, 255), "dark_grey": (105, 105, 105)}


def binomial(n, k):
    """
    calculates the binomial coefficient
    :param n: number 1
    :param k: number 2
    :return: result
    """
    return fac(n) / (fac(n - k) * fac(k))
