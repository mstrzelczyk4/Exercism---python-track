from math import gcd
from string import ascii_lowercase as alphabet


def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime!')
    encoded = []
    for c in plain_text:
        if c.lower() in alphabet:
            encoded.append(alphabet[(a * alphabet.index(c.lower()) + b) % 26])
        elif c.isdigit():
            encoded.append(c)
    x = 5
    while x < len(encoded):
        encoded.insert(x, " ")
        x += 6
    return "".join(encoded)


def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime!')
    decoded = []
    mmi = 1
    while a * mmi % 26 != 1:
        mmi += 1
    for c in ciphered_text:
        if c in alphabet:
            decoded.append(alphabet[mmi * (alphabet.index(c) - b) % 26])
        elif c.isdigit():
            decoded.append(c)
    return "".join(decoded)
