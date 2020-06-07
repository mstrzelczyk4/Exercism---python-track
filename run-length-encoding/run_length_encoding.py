def decode(string):
    if not string:
        return ""
    decoded = ""
    tmp = ""
    for c in string:
        if c.isdigit():
            tmp += c
        else:
            decoded += c if tmp == "" else "{}".format((int(tmp)) * c)
            tmp = ""
    return decoded


def encode(string):
    if not string:
        return ""
    count = 0
    tmp = string[0]
    encoded = ""
    for c in string:
        if c == tmp:
            count += 1
        else:
            encoded += add_string(count, tmp)
            tmp = c
            count = 1
    encoded += add_string(count, tmp)
    return encoded


def add_string(count, tmp):
    str = ""
    if count > 1:
        str += "{}".format(count)
    str += tmp
    return str
