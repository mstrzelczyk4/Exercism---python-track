def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("Invalid base!")
    digits.reverse()
    return convert_to_output(convert_to_decimal(digits, input_base), output_base)


def convert_to_decimal(digits, input_base):
    number_here = 0
    for i, num in enumerate(digits):
        if num < 0 or num >= input_base:
            raise ValueError("Invalid digits!")
        number_here += num * input_base ** i
    return number_here


def convert_to_output(number, output_base):
    out = []
    while number:
        out.append(number % output_base)
        number //= output_base
    if not out:
        return [0]
    return out[::-1]
