def convert(input_grid):
    if len(input_grid) % 4 != 0 or len(input_grid[0]) % 3 != 0:
        raise ValueError("Error")
    input = {
        "   ": "0",
        " _ ": "1",
        "  |": "2",
        " _|": "3",
        "|_|": "4",
        "|_ ": "5",
        "| |": "6",
    }
    number = []
    for i in range(len(input_grid)):
        number.append("")
        for j in range(int(len(input_grid[0]) / 3)):
            try:
                number[i] += input[input_grid[i][j*3:j*3+3]]
            except KeyError:
                number[i] += "?"
    return give_number(number)


def give_number(number):
    num = ""
    i = 0
    while i < len(number):
        for j in range(len(number[0])):
            nr = number[i][j] + number[i+1][j] + number[i+2][j] + number[i+3][j]
            if nr == "1640":
                num += "0"
            elif nr == "0220":
                num += "1"
            elif nr == "1350":
                num += "2"
            elif nr == "1330":
                num += "3"
            elif nr == "0420":
                num += "4"
            elif nr == "1530":
                num += "5"
            elif nr == "1540":
                num += "6"
            elif nr == "1220":
                num += "7"
            elif nr == "1440":
                num += "8"
            elif nr == "1430":
                num += "9"
            else:
                num += "?"
        num += ","
        i += 4
    return num[:-1]
