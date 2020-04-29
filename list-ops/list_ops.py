def append(list1, list2):
    return list1 + list2


def concat(lists):
    final_list = []
    for elem in lists:
        final_list += elem
    return final_list


def filter(function, list):
    return [elem for elem in list if function(elem)]


def length(list):
    return sum([1 for elem in list])


def map(function, list):
    return [function(elem) for elem in list]


def foldl(function, list, initial):
    for elem in list:
        initial = function(initial, elem)
    return initial


def foldr(function, list, initial):
    for elem in reversed(list):
        initial = function(elem, initial)
    return initial


def reverse(list):
    return list[::-1]
