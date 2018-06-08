from utils import *
from graham import graham
from copy import deepcopy


def secteur_angulaire(point, subset):
    return 0

def raccord(subset1, subset2):
    p = [0,0]
    s1 = deepcopy(subset1)
    s2 = deepcopy(subset2)
    n1 = len(subset1)
    # pour trouver un point p à l'intérieur de l'enveloppe convexe de subset1,
    #  j'ai choisi de faire la moyenne des points
    for point in s1:
        p[0] += point[0]
        p[1] += point[1]
    p[0] / n1
    p[1] /= n1
    if point_in_polygon(p, subset1):
        jointure = s1 + s2
    else:
        h = s2[0]
        b = s2[0]
        #theta = angle()
        jointure = s1 + s2
    return graham(jointure)


    return 0


def shamos(points):
    n = len(points)
    if n <= 3:
        return polar_quicksort(points, [0,0])
    else:
        return raccord(shamos(points[:n//2]), shamos(points[n//2:]))

