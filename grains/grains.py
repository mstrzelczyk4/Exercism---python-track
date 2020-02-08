def square(number):
    if number not in range(1, 65):
        raise ValueError("Invalid number")
    return 1 << (number - 1)


def total():
    return 2**64 - 1
