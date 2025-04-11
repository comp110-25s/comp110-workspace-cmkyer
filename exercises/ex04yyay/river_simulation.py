__author__: str = "730822368"


# from exercises.ex04.river import River

# CHANGE TO EX UPPERCASE
from exercises.EX04.river import River

my_river: River = River(num_fish=10, num_bears=2)

my_river.view_river()

my_river.one_river_week()

my_river.one_river_day()

my_river.remove_fish(5)

my_river.check_ages()

my_river.bears_eating()

my_river.check_hunger()

my_river.repopulate_fish()

my_river.repopulate_bears()
