# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = x, y

    def move(self, run):
        for step in run:
            if step == "R":
                if self.direction == 1:
                    self.direction = 5
                self.direction -= 1
            elif step == "L":
                if self.direction == 4:
                    self.direction = 0
                self.direction += 1
            else:
                if self.direction == 1:
                    self.coordinates = self.coordinates[0] + 1, self.coordinates[1]
                elif self.direction == 2:
                    self.coordinates = self.coordinates[0], self.coordinates[1] + 1
                elif self.direction == 3:
                    self.coordinates = self.coordinates[0] - 1, self.coordinates[1]
                else:
                    self.coordinates = self.coordinates[0], self.coordinates[1] - 1
