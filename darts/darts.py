import math


def score(x, y):
    result = math.sqrt(x**2 + y**2)
    if result > 10:
        return 0
    elif result > 5:
        return 1
    elif result > 1:
        return 5
    else:
        return 10
