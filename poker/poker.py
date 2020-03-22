def best_hands(hands):
    values = [give_value(i) for i in hands]
    w = max(i for i in values)
    return [hands[i] for i in range(len(hands)) if values[i][1] == w[1]]


def give_value(hand):
    value = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    cards = sorted([[x[:-1], x[-1]] for x in hand.split()])
    colors = [x[1] for x in cards]
    values = sorted([value[x[0]] for x in cards])
    length = len(set(values))
    if (len(set(colors)) == 1 and length == 5) and values[4] - values[0] == 4:
        return 9, values[4]
    elif length == 2 and values[1] == values[3]:
        return 8, values[0] ** values.count(values[0]) + values[4] ** values.count(values[4])
    elif length == 2 and values[1] != values[3]:
        return 7, values[0] * (10 ** values.count(values[0])) + values[4] * (10 ** values.count(values[4]))
    elif len(set(colors)) == 1:
        return 6, values[4]
    elif length == 5 and (values[4] - values[0] == 4 or values[4] - values[3] == 9):
        return 5, values[0] * 2 - values[4]
    elif length == 3 and values.count(values[2]) == 3:
        return 4, values[2] * 5 + sum(set(values))
    elif length == 3:
        return 3, values[1] ** 6 + values[3] ** 6 + min(values, key=values.count)
    elif length == 4:
        return 2, max(values, key=values.count)
    else:
        return 1, sum(x ** 6 for x in set(values))



