from utils import *


def find_start_point(points):
    x_min = float("inf")
    x_max = float("-inf")
    p_min = []
    p_max = []
    for point in points:
        if x_min > point[0]:
            x_min = point[0]
            p_min = point
        if x_max < point[0]:
            x_max = point[0]
            p_max = point
    if len(points) > 1:
        points.pop(points.index(p_min))
        points.pop(points.index(p_max))
    return p_min, p_max


def next_point(point1, point2, points):
    line = [point1, point2]
    dist = 0
    p = []
    for point in points:
        if distance_from_point_to_line(point, line) > dist:
            dist = distance_from_point_to_line(point, line)
            p = point
    return p


def sup_line(point1, point2, points):
    points_sup = []
    for point in points:
        if determinant(point1, point2, point) > 0:
            points_sup.append(point)
    return points_sup


def inf_line(point1, point2, points):
    points_inf = []
    for point in points:
        if determinant(point1, point2, point) < 0:
            points_inf.append(point)
    return points_inf


def remove_duplicate(l):
    final_l = []
    for ele in l:
        if ele not in final_l:
            final_l.append(ele)
    return final_l


def eddy_floyd_rec(points, p_min, p_max, show = False):
    if points:
        points_sup = sup_line(p_min, p_max, points)
        points_inf = inf_line(p_min, p_max, points)
        point_sup = next_point(p_min, p_max, points_sup)
        point_inf = next_point(p_min, p_max, points_inf)
        if len(points_sup) > 1:
            points_sup.pop(points_sup.index(point_sup))
            points_sup_left = sup_line(p_min, point_sup, points_sup)
            points_sup_right = sup_line(point_sup, p_max, points_sup)
        else:
            points_sup_left = []
            points_sup_right = []
        if len(points_inf) > 1:
            points_inf.pop(points_inf.index(point_inf))
            points_inf_left = inf_line(p_min, point_inf, points_inf)
            points_inf_right = inf_line(point_inf, p_max, points_inf)
        else:
            points_inf_left = []
            points_inf_right = []
        if points_sup != [] and points_inf != []:
            subset = [p_min] + eddy_floyd_rec(points_sup_left, p_min, point_sup) + [point_sup] + eddy_floyd_rec(points_sup_right, point_sup, p_max) + [p_max ] + eddy_floyd_rec(points_inf_right, p_max, point_inf) + [point_inf] + eddy_floyd_rec(points_inf_left, point_inf, p_min)
            if show == True:
                 scatter_plot(points, [subset], title="exhaustive search", show=True, save=False)
            return subset
        elif points_sup != [] and points_inf == []:
            subset = [p_min] + eddy_floyd_rec(points_sup_left, p_min, point_sup) + [point_sup] + eddy_floyd_rec(points_sup_right, point_sup, p_max) + [p_max]
            if show == True:
                 scatter_plot(points, [subset], title="exhaustive search", show=True, save=False)
            return subset
        elif points_sup == [] and points_inf != []:
            subset =  [p_max] + eddy_floyd_rec(points_inf_right, p_max, point_inf) + [point_inf] + eddy_floyd_rec(points_inf_left, point_inf, p_min) + [p_min]
            if show == True:
                 scatter_plot(points, [subset], title="exhaustive search", show=True, save=False)
            return subset
        else:
            return []

    else:
        return []


def eddy_floyd(points, show=False):
    p_min, p_max = find_start_point(points)
    hull = polar_quicksort(eddy_floyd_rec(points, p_min, p_max, show = show),[25,25])
    hull = remove_duplicate(hull)
    return hull


