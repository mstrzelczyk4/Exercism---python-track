class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergen = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"
        }

    def allergic_to(self, item):
        if not self.give_key(item) & self.score:
            return False
        elif self.allergen[self.give_key(item) & self.score] == item:
            return True
        return False

    def give_key(self, key):
        for x in self.allergen:
            if self.allergen[x] == key:
                return x

    @property
    def lst(self):
        return [self.allergen[key] for key in self.allergen if key & self.score]
