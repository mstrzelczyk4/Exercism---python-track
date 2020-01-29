import random
import string


class Robot:
    used_names = set()
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = self.generate_new_random_name()
        self.used_names.add(self.name)

    def random_name(self):
        return f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}" \
               f"{random.randrange(0,9)}{random.randrange(0,9)}{random.randrange(0,9)}"

    def generate_new_random_name(self):
        while True:
            new_random_name = self.random_name()
            if new_random_name not in self.used_names:
                return new_random_name

