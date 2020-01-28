def is_pangram(sentence):
    sentence = sentence.lower()
    for x in "abcdefghijklmnopqrstuvwxyz":
        if x not in sentence:
            return False
    return True
