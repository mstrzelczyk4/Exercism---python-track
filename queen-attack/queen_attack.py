class Queen:
    def __init__(self, row, column):
        if row in range(0, 8) and column in range(0, 8):
            self.row = row
            self.column = column
        else:
            raise ValueError("Row and/or column invalid value")

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Two queens at the same pool!")
        if self.row == another_queen.row or self.column == another_queen.column or abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False
