from collections import defaultdict


class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        return [name for key in sorted(self.students.keys()) for name in sorted(self.students[key])]

    def grade(self, grade_number):
        return sorted(self.students[grade_number])
