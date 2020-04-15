from math import floor


def find(search_list, value):
    l = 0
    r = len(search_list)
    if not r:
        raise ValueError("Empty list!")
    if not search_list[0] <= value <= search_list[r - 1]:
        raise ValueError("Value not in list!")
    while l <= r:
        m = floor((l + r) / 2)
        if search_list[m] < value:
            l = m + 1
        elif search_list[m] > value:
            r = m - 1
        else:
            return m
    raise ValueError("Value not found!")