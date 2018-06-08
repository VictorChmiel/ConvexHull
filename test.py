from random import seed

from exhaustive import exhaustive
from utils import create_points, scatter_plot
from graham import *
from jarvis import *
from eddy_floyd import *
from shamos import *

def main():
    """
    A sample main program to test our algorithms.

    @return: None
    """
    # initialize the random generator seed to always use the same set of points
    seed(0)
    # creates some points
    pts = create_points(6)
    show = True  # to display a frame
    save = False  # to save into .png files in "figs" directory
    scatter_plot(pts, [[]], title="convex hull : initial set", show=show, save=save)
    print("Points:", pts)
    # compute the hull
    #hull = exhaustive(pts, show=show, save=save)
    hull = graham(pts, show=show, save=save)
    #hull = jarvis(pts, show=show, save=save)
    #hull = eddy_floyd(pts)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=True, save=save)


if __name__ == "__main__":
    main()
