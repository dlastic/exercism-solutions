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


def color_code(color: str) -> int:
    """Return the numeric code for the given resistor color."""
    return COLOR_LIST.index(color)


def colors() -> list:
    """Return the list of all resistor colors."""
    return COLOR_LIST
