plant = {
    "C": "Clover",
    "G": "Grass",
    "R": "Radishes",
    "V": "Violets"
}


class Garden:
    def __init__(self, diagram, students=None):
        self.rows = diagram.split("\n")
        self.students = sorted(students or ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"])
        self.studs = {name: i for i, name in enumerate(self. students)}

    def plants(self, name):
        x = self.studs[name]
        return [plant[self.rows[0][x * 2]], plant[self.rows[0][x * 2 + 1]], plant[self.rows[1][x * 2]], plant[self.rows[1][x * 2 + 1]]]
