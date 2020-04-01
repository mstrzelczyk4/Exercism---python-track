plain = "abcdefghijklmnopqrstuvwxyz0123456789"
cipher = "zyxwvutsrqponmlkjihgfedcba0123456789"


def encode(plain_text):
    transtab = str.maketrans(plain, cipher)
    encoded = [c.translate(transtab) for c in plain_text.lower() if c in plain]
    x = 5
    while x < len(encoded):
        encoded.insert(x, " ")
        x += 6
    return "".join(encoded)


def decode(ciphered_text):
    transtab = str.maketrans(cipher, plain)
    return "".join([c.translate(transtab) for c in ciphered_text if c in plain])
