from random import choice
from string import ascii_lowercase


def rand_string(string_length):
    letters = ascii_lowercase
    return ''.join(choice(letters) for i in range(string_length))


class Cipher:
    def __init__(self, key=None):
        if not key:
            key = rand_string(100)
        self.key = key

    def encode(self, text):
        return ''.join(chr((ord(char) + ord(self.key[index % len(self.key)]) - 2 * 97) % 26 + 97) for index, char in
                       enumerate(text))

    def decode(self, text):
        return ''.join(
            chr((ord(char) - ord(self.key[index % len(self.key)])) % 26 + 97) for index, char in enumerate(text))