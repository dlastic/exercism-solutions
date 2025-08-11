def square(number: int) -> int:
    """Return the number of grains on a specific square of a chessboard."""
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    """Return the total number of grains on the chessboard."""
    return 2 ** 64 - 1
