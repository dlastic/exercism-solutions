BAND_COLORS = [
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
    return BAND_COLORS.index(color)


def colors() -> list:
    """Return the list of all resistor colors."""
    return BAND_COLORS
