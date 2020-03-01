from collections import Counter
import re


def count_words(sentence):
    return Counter([x.strip("''") for x in re.compile("[A-Za-z0-9']+").findall(sentence.lower())])
