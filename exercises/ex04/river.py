__author__: str = "730822368"


"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]
    hunger_score: int

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """identifies when fish and bears reach a certain age and die"""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def bears_eating(self):
        """removes a certain number of fish that the bear eats"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """removes bears whose hunger score gets too low"""
        new_bears: list[Bear] = []
        self.hunger_score: int
        for bear in self.bears:
            if self.hunger_score < 0:
                new_bears.append(bear)
        self.bears = new_bears

    def repopulate_fish(self):
        """models reproduction of fish"""
        baby_fish = len(self.fish) // 2
        for __ in range(baby_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """models reproduction of bears"""
        baby_bears = (len(self.bears) // 2) * 4
        for __ in range(baby_bears):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Tells us the populations of bears and fish on a given day"""
        print(f"~~~Day {self.day}:~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """tells us how bear and fish pops change throughout a week"""
        count = 0
        while count < 7:
            self.one_river_day()
            count += 1
        return

    def remove_fish(self, amount: int):
        """removes fish when they are eaten or die of old age"""
        for fish in self.fish:
            idx: int = 0
            amount = 0
            while idx < amount:
                self.fish.pop(idx)
                idx += 1
