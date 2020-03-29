def rotate(text, key):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in text:
        if c.lower() in alphabet:
            ind = alphabet.index(c.lower()) + key
            if ind > 25:
                ind -= 26
            if c.islower():
                result += alphabet[ind]
            else:
                result += alphabet[ind].upper()
        else:
            result += c
    return result
