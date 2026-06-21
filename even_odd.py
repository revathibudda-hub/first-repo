def even_or_odd(number):
    """Return 'even' if the number is even, otherwise return 'odd'."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    return "even" if number % 2 == 0 else "odd"


if __name__ == "__main__":
    example_numbers = [0, 1, 2, 15, 24, 99]
    for num in example_numbers:
        result = even_or_odd(num)
        print(f"{num} is {result}")
