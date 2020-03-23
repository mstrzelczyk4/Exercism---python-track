def largest_product(series, size):
    if size == 0:
        return 1
    elif size > len(series) or size < 0:
        raise ValueError("Error")
    return max([multiply(series[start:start + size]) for start in range(len(series) - size + 1)])


def multiply(num):
    multi = 1
    for c in str(num):
        multi *= int(c)
    return multi
