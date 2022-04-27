from random import random
from math import sqrt, floor

# SPAZIO METRICO
INPUT = [(random()*10, random()*10) for _ in range(1000)]

def dist(p1, p2) -> float:
    """
        Norma euclidea
    """
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_median_point(X):
    """
        Returns the median point of the set of points X.
    """
    return sorted(X, key=lambda p: p[0])[floor(len(X)/2)]

def min_dist(X) -> float:
    if len(X) == 1:
        return float("inf")
    if len(X) == 2:
        return dist(X[0], X[1])

    # ordina rispetto alle coordinate x
    X.sort(key=lambda p: p[0])
    min_left = min_dist(X[:floor(len(X)/2)])
    min_right = min_dist(X[floor(len(X)/2):])

    r = min(min_left, min_right)
    median = find_median_point(X)
    new_X = list(filter(lambda p: p[0] >= median[0]-r or p[0] <= median[0], X))

    new_X.sort(key=lambda p: p[1])
    dists = []
    for i in range(0, len(new_X)-10):
        dists.append(min(list(map(lambda p: dist(p, new_X[i]), new_X[i+1:i+11]))))
    return min(min_left, min_right, *dists)

def trivial_alg(X):
    min_dist = float("inf")
    for i in range(len(X)-1):
        for j in range(i+1, len(X)):
            min_dist = min(min_dist, dist(X[i], X[j]))
    return min_dist

errors = 0
for i in range(1000):
    INPUT = [(random()*10, random()*10) for _ in range(1000)]
    print(f"SIMULAZIONE: {i}")
    alg, trivial = min_dist(INPUT), trivial_alg(INPUT)
    if alg != trivial:
        print("CAZZO")
        print(alg, trivial)
        errors += 1

print(f"errors: {errors}")
