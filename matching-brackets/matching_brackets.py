pairs = {
    '}': '{',
    ']': '[',
    ')': '('
}


def is_paired(input_string):
    stack = []
    for ch in input_string:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs.keys():
            if len(stack) and stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False
    return not stack
