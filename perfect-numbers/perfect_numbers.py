def classify(number):
    if number < 1:
        raise ValueError("Error")
    factors = []
    for x in range(1, int(number / 2 + 1)):
        if number % x == 0:
            factors.append(x)
    if sum(factors) == number:
        return "perfect"
    elif sum(factors) > number:
        return "abundant"
    else:
        return "deficient"
