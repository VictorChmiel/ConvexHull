from utils import *


def start_point(points):
    """
    :param points: List of point (x,y)
    :return: Return the point at the bottom left corner
    """
    x_min = float("inf")
    y_min = float("inf")
    i = 0
    n = len(points)
    for j in range(n):
        x = points[j][0]
        y = points[j][1]
        if x < x_min and y < y_min:
            x_min = x
            y_min = y
            i = j
    point = points[i]
    points.pop(i)
    return point


def graham(points):
    """

    :type points: List of point (x,y)
    :return Run the Graham's algorithm
    """
    point = start_point(points)
    points = polar_quicksort(points, point)
    hull = [point]
    for point in points:
        while len(hull) > 1 and determinant(hull[-2], hull[-1], point) < 0:
            hull.pop()
        hull.append(point)
    return hull
