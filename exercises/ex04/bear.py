"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age: int = 0
        hunger_score: int = 0
        return None

    def one_day(self):
        self.age += 1
        hunger_score -= 1
        return self.age

    def eat(self, num_fish: int):
        hunger_score += len(num_fish)
