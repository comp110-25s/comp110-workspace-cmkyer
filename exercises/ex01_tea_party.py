"""Planning the resources needed for a cozy tea party"""

__author__: str = "730822368"


def main_planner(guests: int) -> None:
    """Main function to produce and call all function outputs for the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """The number of tea bags needed for a certain number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats based on number of teas guests are expected to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of teabags and treats needed"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
