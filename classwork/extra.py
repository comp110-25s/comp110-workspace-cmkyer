def icarus(x: int) -> int:
    print(f"Height: {x}")
    return icarus(x=x + 1)


def safe_icarus(x: int) -> int:
    if x >= 2:
        return 1
    else:
        return 1 + safe_icarus(x=x + 1)


print(safe_icarus(x=0))
