num = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def roman(number):
    result = ""
    if number > 900:
        result += give_nums(1000, int(number / 1000) % 10)
    if number > 90:
        result += give_nums(100, int(number / 100) % 10)
    if number > 9:
        result += give_nums(10, int(number / 10) % 10)
    result += give_nums(1, number % 10)
    return result


def give_nums(multi, rest):
    number = rest * multi
    if number < 4 * multi:
        return num[1 * multi] * rest
    elif number == 4 * multi:
        return num[1 * multi] + num[5 * multi]
    elif number < 9 * multi:
        return num[5 * multi] + num[1 * multi] * (rest - 5)
    elif number == 9 * multi:
        return num[1 * multi] + num[10 * multi]