def commands(number):
    comm = {
        1: "wink",
        2: "double blink",
        4: "close your eyes",
        8: "jump"
    }
    tab = [comm[key] for key in comm if key & number]
    if number & 16:
        return tab[::-1]
    else:
        return tab
