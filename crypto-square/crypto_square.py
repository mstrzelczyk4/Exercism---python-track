from math import ceil, sqrt


def cipher_text(plain_text):
    text = [c.lower() for c in plain_text if c.isalpha() or c.isdigit()]
    column = ceil(sqrt(len(text)))
    if column * (column - 1) >= len(text):
        row = column - 1
    else:
        row = column
    text_ciphered = []
    for x in range(0, column):
        for y in range(0, row):
            try:
                text_ciphered.append(text[x + y * column])
            except:
                text_ciphered.append(" ")
    for x in range(column - 1, 0, -1):
        text_ciphered.insert(x * row, " ")
    return "".join(text_ciphered)
