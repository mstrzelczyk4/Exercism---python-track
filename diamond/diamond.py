def rows(letter):
    nr = ord(letter) - 65
    diamond = ["{}A{}".format(" " * nr, " " * nr)]
    if nr:
        for i in range(1, nr):
            diamond.append(give_line(nr, i))
        for i in range(nr, 0, -1):
            diamond.append(give_line(nr, i))
        diamond.append("{}A{}".format(" " * nr, " " * nr))
    return diamond


def give_line(nr, i):
    return "{}{}{}{}{}".format(" " * (nr - i), chr(65 + i), " " * (2 * i - 1), chr(65 + i), " " * (nr - i),)
