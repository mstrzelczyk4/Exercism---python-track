class Matrix:
    def __init__(self, matrix_string):
        self.lines = [i.split() for i in matrix_string.split('\n')]

    def row(self, index):
        return [int(i) for i in self.lines[index - 1]]

    def column(self, index):
        return [int(self.lines[i][index - 1]) for i in range(len(self.lines))]
