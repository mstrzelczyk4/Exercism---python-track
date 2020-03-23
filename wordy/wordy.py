import re


def answer(question):
    operators = ["plus", "minus", "multiplied", "divided"]
    tab = [word for word in question[:-1].split() if re.search("[0-9]+", word) or word in operators]
    if len(tab) % 2 == 0 or not re.search("[0-9]+", question[-2]):
        raise ValueError("Invalid question!")
    for x in range(len(tab)):
        if x % 2 == 0:
            try:
                tab[x] = int(tab[x])
            except ValueError:
                raise ValueError("Invalid question!")
        elif tab[x] not in operators:
            raise ValueError("Invalid question!")

    if len(tab) == 1:
        return tab[0]
    result = tab[0]
    i = 1
    while i < len(tab):
        if tab[i] == "plus":
            result += tab[i + 1]
        elif tab[i] == "minus":
            result -= tab[i + 1]
        elif tab[i] == "multiplied":
            result *= tab[i + 1]
        elif tab[i] == "divided":
            result /= tab[i + 1]
        i += 2
    return result
