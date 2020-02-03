def is_valid(isbn):
    isbn = isbn.split('-')
    isbn_split = [x for y in range(len(isbn)) for x in isbn[y]]
    if len(isbn_split) != 10:
        return False
    for x in range(9):
        if not isbn_split[x].isdigit():
            return False
    if isbn_split[9] == 'X':
        last = 10
    elif not isbn_split[9].isdigit():
        return False
    else:
        last = int(isbn_split[9])
    return (sum((int(isbn_split[x]) * (10 - x)) for x in range(9)) + last) % 11 == 0
