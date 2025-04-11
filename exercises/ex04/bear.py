__author__: str = "730822368"


"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """tells us the age and hunger of bears on a given day"""
        self.age += 1
        self.hunger_score -= 1
        return self.age

    def eat(self, num_fish: int):
        """updates a bear's hunger score by the number of fish it eats"""
        self.hunger_score += num_fish
        return self.hunger_score
