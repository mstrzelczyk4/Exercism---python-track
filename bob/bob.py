import re


def response(hey_bob):
    tab = [True for ch in hey_bob if ch.isalpha() and ch.islower()]
    question = hey_bob.strip().endswith('?')
    alpha = re.search('[a-zA-Z]', hey_bob)
    digits = re.search('[1-9]', hey_bob)
    if not alpha and not question and not digits:
        return "Fine. Be that way!"
    elif not tab and question and alpha:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif not tab and alpha:
        return "Whoa, chill out!"
    else:
        return "Whatever."
