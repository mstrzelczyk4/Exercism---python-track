num = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
    1000: "one thousand",
    1000000: "one million",
    1000000000: "one billion"
}


def say(number):
    if 999999999999 < number or number < 0:
        raise ValueError("Value out of range!")
    part_of_num = []
    if number in num:
        return num[number]
    elif number > 0:
        part_of_num.append(give_num(number % 1000))
    if number > 1000:
        part_of_num.append(give_num(int(number / 1000) % 1000) + " thousand")
    if number > 1000000:
        part_of_num.append(give_num(int(number / 1000000) % 1000) + " million")
    if number > 1000000000:
        part_of_num.append(give_num(int(number / 1000000000) % 1000) + " billion")
    part_of_num.reverse()
    return " ".join(item for item in part_of_num if item)


def give_num(number):
    if 0 < number < 21:
        return num[number]
    if 100 > number > 20:
        return num[int(number / 10) * 10] + "-" + num[number % 10]
    return give_num(int(number / 100) % 10) + " hundred " + give_num(number % 100)
