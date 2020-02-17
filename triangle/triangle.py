def equilateral(sides):
    if len(set(sides)) == 1 and sides[0] != 0:
        return True
    else:
        return False


def isosceles(sides):
    nr = set(sides)
    if len(nr) == 1 or (len(nr) == 2 and min(nr) * 2 > max(nr)):
        return True
    else:
        return False


def scalene(sides):
    nr = set(sides)
    if len(nr) == 3 and sum(nr) / 2 > max(nr):
        return True
    else:
        return False
