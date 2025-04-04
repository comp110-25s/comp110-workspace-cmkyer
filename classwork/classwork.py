def perimeter(length: float, width: float) -> float:
    print(2 * length + 2 * width)
    return 2 * length + 2 * width


perimeter(10.0, 54.8)


def total_cost(price: int, tax_rate: float) -> float:
    print(price + (price * tax_rate))


print(total_cost(price=100, tax_rate=0.07))


def total_cost(price: int, tax_rate: float) -> float:
    return price + (price * tax_rate)


print(total_cost(price=100, tax_rate=0.07))


def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))
