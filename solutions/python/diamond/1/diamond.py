import string


def rows(letter: str) -> list[str]:
    """Return letters from A to the input letter in a diamond shape."""
    letters = string.ascii_uppercase
    if not letter or letter not in letters:
        raise ValueError("Input must be a single uppercase letter")
    target_letters = letters[: letters.index(letter) + 1]

    num_letters = len(target_letters)
    grid_size = num_letters * 2 - 1
    center = num_letters - 1
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

    for i, char in enumerate(target_letters):
        # Top half
        grid[i][center - i] = char
        grid[i][center + i] = char
        # Bottom half
        bottom_row = grid_size - 1 - i
        grid[bottom_row][center - i] = char
        grid[bottom_row][center + i] = char

    return ["".join(line) for line in grid]
