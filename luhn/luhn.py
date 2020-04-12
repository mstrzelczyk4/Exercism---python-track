class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num = "".join(self.card_num.split())
        if not num.isdigit() or len(num) < 2:
            return False
        sum = 0
        for i, x in enumerate(num[::-1]):
            x = int(x)
            if i % 2 == 0:
                sum += x
            elif x * 2 > 9:
                sum += x * 2 - 9
            else:
                sum += x * 2
        return sum % 10 == 0
