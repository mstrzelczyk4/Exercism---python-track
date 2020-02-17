def is_isogram(string):
    buf = [ch for ch in string.lower() if ch.isalpha()]
    buf2 = set(buf)
    return len(buf) == len(buf2)
