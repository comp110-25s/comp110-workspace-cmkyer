"""Exercise 3 - Practicing Dictionary Functions"""

__author__: str = "730822368"


# Dictionary assigning an activity to a season
def invert(a: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary where the key and value are flipped from the original"""
    # inverts: dict[str, str] = {"skiing": "winter","picnic": "spring","hay ride":
    # "fall","pool party": "summer"}

    flipped: dict[str, str] = {}

    # k and v = keys and variables
    # identify keys and values and print them flipped

    for key, value in a.items():
        if value in flipped:
            raise KeyError(f"Duplicate Value Found: {value}")
        else:
            flipped[value] = key
    return flipped


print(invert({}))


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value is listed in a list of strings"""
    # values: list[str] = ["cat", "dog", "gerbil", "cat"]
    result: dict[str, int] = {}

    for string in values:

        if string in result:
            result[string] += 1
        else:
            result[string] = 1
    return result


print(count([]))


def favorite_color(favs: dict[str, str]) -> str:
    """Returns the most common color from a dictionary of strings"""
    # {"charlotte": "purple","brooke": "yellow", "catherine": "pink","morgan": "purple"}
    counts = {}
    max_ct = 0
    most_common = ""

    for key in favs:
        favorite_color = favs[key]
        if favorite_color in counts:
            counts[favorite_color] += 1
        else:
            counts[favorite_color] = 1
        if counts[favorite_color] > max_ct:
            most_common = favorite_color
            max_ct = counts[favorite_color]
    return most_common


print(favorite_color({}))


def bin_len(input: list[str]) -> dict[int, set[str]]:
    """Puts list of strings into a dictionary and counts the length"""
    leng: int = 0
    bin: dict[int, set[str]] = {}

    for string in input:
        leng = len(string)
        if leng not in bin:
            bin[leng] = set()
        bin[leng].add(string)
    return bin


print(bin_len([]))
