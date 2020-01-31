def is_armstrong_number(number):
    num_str = [int(i) for i in str(number)]
    result = 0
    for i in num_str:
        result += int(i) ** len(num_str)
    if number == result:
        return True
    else:
        return False
