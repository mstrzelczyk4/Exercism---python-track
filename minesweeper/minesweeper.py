import re


def annotate(minefield):
    rows_len = []
    if not minefield:
        return []
    elif minefield == [""]:
        return [""]
    for row in minefield:
        rows_len.append(len(row))
        if re.match(r"(?!([\d| |\*|^$]))", row):
            raise ValueError("Invalid input data!")
    if len(set(rows_len)) > 1:
        raise ValueError("Invalid input data!")
    result = []
    line = ""
    i = 1
    for c in [check_pools(minefield, x, y) for x in range(0, len(minefield)) for y in range(0, len(minefield[0]))]:
        line += str(c)
        if not i % len(minefield[0]):
            result.append(line)
            line = ""
        i += 1
    return result


def check_pools(minefield, x, y):
    if minefield[x][y] == "*":
        return "*"
    value = sum([1 for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if check_cond(minefield, x, y, i, j)])
    if value:
        return value
    return " "


def check_cond(minefield, x, y, i, j):
    if 0 <= i < len(minefield) and 0 <= j < len(minefield[0]):
        if minefield[i][j] == "*" and not (x == i and y == j):
            return True
    else:
        return False
