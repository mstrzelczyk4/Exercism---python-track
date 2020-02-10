def steps(number):
    i = 0
    if number < 1:
        raise ValueError("Negative number")
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        i += 1
    return i
