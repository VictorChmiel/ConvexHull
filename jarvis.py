from utils import *


def next_point(points, point):
    """

    :param points: List of point (x,y)
    :param point: point in the hull
    :return: The next point in the hull
    """
    q = point
    for p in points:
        if determinant(point, q, p) < 0 or (determinant(point, q, p) == 0 and distance(point, p) > distance(point, q)):
            q = p
    return q


def jarvis(points):
    """

    :param points: List of point (x,y)
    :return: Run the jarvis algorithm
    """
    points.sort()
    hull = [points[0]]

    for p in hull:
        q = next_point(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull
