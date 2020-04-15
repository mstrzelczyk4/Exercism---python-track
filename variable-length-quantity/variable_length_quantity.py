def encode(values):
    result = []
    for value in values:
        x = []
        while True:
            x.append(value % 128)
            value = value // 128
            if not value:
                break
        for i in range(1, len(x)):
            x[i] += 128
        result.extend(reversed(x))
    return result


def decode(values):
    result = []
    current = 0
    y = 0
    for value in values:
        if not (0 <= value < 256):
            raise ValueError('Value out of range')
        y = value // 128
        current = current * 128 + value % 128
        if not y:
            result.append(current)
            current = 0
    if y == 1:
        raise ValueError('Last zero block not found')
    return result
