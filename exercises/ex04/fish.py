__author__: str = "730822368"


"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        self.age: int = 0
        return None

    def one_day(self) -> None:
        """Tells us the age of fish on a given day."""
        self.age += 1
