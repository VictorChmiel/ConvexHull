from random import seed
from time import time

from exhaustive import exhaustive
from utils import *


def benchmark(sizes=(10, 100, 1000, 10000, 100000), runs=100, method=exhaustive):
    """
    For each size in the 'sizes' list, compute the average time over a given number of runs to find the convex hull
    for a dataset of that size,
    the range used for max and min for the create_points function is always 10 times the highest value in the 'sizes'
    list.

    :param sizes: list of problem sizes to consider (default is (10, 100, 1000, 10000, 100000))
    :param method: the name of the algorithm to use (default is exhaustive)
    :param runs: the number of repetition to perform for computing average (default is 100)
    :return: nothing
    """
    print(method.__name__)
    for s in sizes:
        tot = 0.0
        for _ in range(runs):
            points = create_points(s, 0, max(sizes) * 10)
            t0 = time.time()
            method(points, False)
            tot += (time.time() - t0)
        print("size %d time: %0.5f" % (s, tot / float(runs)))


def main():
    """
    A sample main program.

    :return: nothing
    """
    seed(0)
    algorithms = [exhaustive]  # [graham, jarvis, shamos]

    for algorithm in algorithms:
        benchmark(sizes=range(2, 10, 2), runs=10, method=algorithm)


if __name__ == "__main__":
    main()
