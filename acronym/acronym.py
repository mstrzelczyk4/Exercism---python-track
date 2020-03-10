import re


def abbreviate(words):
    return "".join([x[0] for x in re.findall("[a-zA-Z']+", words.upper())])
