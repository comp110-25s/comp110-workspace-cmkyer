"""File to define Bear class."""

__author__: str = "730822368"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Tells us the age and hunger of bears on a given day."""
        self.age += 1
        self.hunger_score -= 1
        return self.age

    def eat(self, num_fish: int):
        """Updates a bear's hunger score by the number of fish it eats."""
        self.hunger_score += num_fish
        return self.hunger_score
