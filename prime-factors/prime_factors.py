def factors(value):
    result = []
    i = 2
    while i - 1 < value:
        while value % i == 0:
            result.append(i)
            value /= i
        i += 1
    return result
