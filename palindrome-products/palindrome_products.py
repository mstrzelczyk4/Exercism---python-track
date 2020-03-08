def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor must be smaller than max_factor.")
    product_max = 0
    factors_max = []
    for x in range(min_factor, max_factor + 1):
        for y in range(x, max_factor + 1):
            product = x * y
            if int(str(product)[::-1]) == product:
                if product >= product_max:
                    if product > product_max:
                        factors_max = []
                    product_max = product
                    factors_max.append([x, y])
    if len(factors_max) < 1:
        return None, []
    return product_max, factors_max


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor must be smaller than max_factor.")
    product_min = max_factor * max_factor
    factors_min = []
    for x in range(min_factor, max_factor + 1):
        for y in range(x, max_factor + 1):
            product = x * y
            if int(str(product)[::-1]) == product:
                if product <= product_min:
                    if product < product_min:
                        factors_min = []
                    product_min = product
                    factors_min.append([x, y])
    if len(factors_min) < 1:
        return None, []
    return product_min, factors_min
