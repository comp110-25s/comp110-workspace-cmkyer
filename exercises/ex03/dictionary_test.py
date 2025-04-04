"""Test Space for Exercise 3  - Practicing Dictionary Functions"""

__author__: str = "730822368"

import pytest

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


# for invert function (edge, use use)
def test_edge_invert() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_use_invert() -> None:
    assert invert({"hay ride": "fall"}) == {"fall": "hay ride"}


def test_use2_invert() -> None:
    assert invert({"cats": "dogs", "up": "down"}) == {"dogs": "cats", "down": "up"}


# for count function (use, use, edge)


def test_count_use() -> None:
    assert count(["cat", "dog", "cat"]) == {"cat": 2, "dog": 1}


def test_count_use2() -> None:
    assert count(["one", "two", "one", "two"]) == {"one": 2, "two": 2}


def test_count_edge() -> None:
    assert count([]) == {}


# for favorite_color function (use, use, edge)


def test_favorite_color_use() -> None:
    assert (
        {"charlotte": "purple", "catherine": "pink", "morgan": "purple", "lan": "pink"}
    ) == "purple"


def test_favorite_color_use2() -> None:
    assert ({"c": "purple", "s": "pink", "m": "purple"}) == "purple"


def test_favorite_color_edge() -> None:
    assert favorite_color({}) == ""


# for bin_len function(use, use, edge)


def test_bin_len_use() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use2() -> None:
    assert bin_len(["charlotte", "happy", "yes"]) == {
        9: {"charlotte"},
        5: {"happy"},
        3: {"yes"},
    }


def test_bin_len_edge() -> None:
    assert bin_len([]) == {}
