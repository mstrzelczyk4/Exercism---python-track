class PhoneNumber:
    number = ""
    area_code = ""


    def __init__(self, number):
        for x in number:
            if x.isdigit():
                self.number += x
        length = len(self.number)
        if length < 10 or length > 11 or (length == 11 and self.number[0] != '1'):
            raise ValueError("Invalid number")
        self.number = self.number[length - 10::]
        self.area_code = self.number[0:3]

        if self.number[0] == '0' or self.number[0] == '1' or self.number[3] == '0' or self.number[3] == '1':
            raise ValueError("Invalid number")
    def pretty(self):
        return f'({self.number[0:3]}) {self.number[3:6]}-{self.number[6:10]}'
