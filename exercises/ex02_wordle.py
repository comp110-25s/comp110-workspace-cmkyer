"""Comp110 Exercise 2: Wordle"""

__author__: str = "730822368"


def contains_char(search: str, one_char: str) -> bool:
    """Search is analyzed by one_char to check if character is in first parameter."""
    assert len(one_char) == 1, f"len('{one_char}') is not 1"

    # checking if the search word contains a specific letter by looping through each character in search until we identify if it contains the character
    i = 0
    while one_char != search[i]:
        if i >= len(search) - 1:
            return False
        else:
            i += 1

    return True


def emojified(guess: str, secret: str) -> str:
    """Calls contains_char to place colored blocks for the correct/incorrect letters"""
    assert len(guess) == len(secret), "Guess must be the same length as secret."

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    i = 1
    box_str: str = ""

    # len starts at 1 and indexing starts at 0, so we even them out by starting i at 1 then subtracting 1 every time
    # loops through every character of the designated length and adds the corresponding box to a printed string
    while len(guess) >= i:
        if contains_char(secret, guess[i - 1]):
            if guess[i - 1] == secret[i - 1]:
                box_str += GREEN_BOX
            else:
                box_str += YELLOW_BOX
        else:
            box_str += WHITE_BOX
        i += 1
    return box_str


def input_guess(expected_len: int) -> str:

    # creates new variable to hold the user's guess
    response: str = input(f"Enter a {expected_len} character word:")

    # loops until the expected length is equal to the length of the user's guess
    while expected_len != len(response):
        response = input(f"That wasn't {expected_len} chars! Try again:")
    return response


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    # tells us what turn the user is on, starting at 1
    turn: int = 1

    # loops until the player reaches 6 turns, then they are unable to continue the game
    while 6 >= turn:
        print(f"=== Turn {turn}/6 ===")
        player_guess = input_guess(len(secret))
        print(emojified(player_guess, secret))

        if player_guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="urmom")
