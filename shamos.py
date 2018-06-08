from utils import *


def raccord(subset1, subset2):
    p = [0,0]
    n1 = len(subset1)
    # pour trouver un point p à l'intérieur de l'enveloppe convexe de subset1,
    #  j'ai choisi de faire la moyenne des points
    for point in subset1:
        p[0] += point[0]
        p[1] += point[1]
    p[0] / n1
    p[1] /= n1
    if point_in_polygon(p, subset1):
        jointure = subset1 + subset2
    return 0


def shamos_rec(points):
    n = len(points)
    if n <= 3:
        return points
    else:
        return raccord(points[:n//2], points[n//2:])

