"""fizzbuzz """


def fizzbuzz(i: int) -> str:
    if i % 3 == 0 and i % 5 == 0:
        return "fizzbuzz"
    else:
        if i % 3 == 0:
            return "fizz"
        else:
            if i % 5 == 0:
                return "buzz"
            else:
                return "none"


print(fizzbuzz(450))
