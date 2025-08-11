COLOR_LIST = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors: list[str]) -> int:
    """Return the resistor value from the first two color bands."""
    return 10 * COLOR_LIST.index(colors[0]) + COLOR_LIST.index(colors[1])
