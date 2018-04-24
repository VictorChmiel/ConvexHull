from utils import *

def start_point(points):

    """
    :param points: List of point (x,y)
    :return: Return the point at the bottom left corner
    """
    x_min = 0
    y_min = 0
    d_min = float("inf")
    i = 0
    n = len(points)
    for j in range (n):
        d = distance([x_min, y_min], points[j])
        if d < d_min:
            d_min = d
            i = j
    points.pop(i)
    return points[i]

def graham(points):
    point = start_point(points)
    polar_quicksort(points, point)
    EC = [point, points[0]]
    k = 1
    pi = math.pi
    n = len(points) + 1
    while k < n:
        EC.append(points[k])
        theta = angle(points[k % n], points[(k+1) % n], points[(k+2) % n])
        if theta > pi:
            points.pop(points[(k+1) % n])
            k -= 1
        else:
            k += 1
    return EC