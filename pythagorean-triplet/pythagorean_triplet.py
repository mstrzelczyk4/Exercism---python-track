def triplets_with_sum(number):
    a = 2
    c = number // 2
    b = number - a - c
    triplets = []
    i = 0
    while a < c - 1:
        while a < b:
            if is_triplet([a, b, c]):
                triplets.append([a, b, c])
            a += 1
            b -= 1
        i += 1
        c = number // 2 - i
        a = 2 + i
        b = number - a - c
    return triplets


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    if triplet[0]**2 + triplet[1]**2 == triplet[2]**2:
        return True
    else:
        return False
