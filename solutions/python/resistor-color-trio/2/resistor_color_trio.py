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

UNITS = [
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
]

def label(colors: list[str]) -> str:
    """Convert a 3-band resistor color code to a resistance value."""
    base_value = 10 * COLOR_LIST.index(colors[0]) + COLOR_LIST.index(colors[1])
    multiplier = 10 ** COLOR_LIST.index(colors[2])
    resistance_ohms = base_value * multiplier
    
    for factor, name in UNITS:
        if resistance_ohms >= factor:
            value = resistance_ohms / factor
            value_str = f"{value:.1f}".rstrip("0").rstrip(".")
            return f"{value_str} {name}"

    return f"{resistance_ohms} ohms"
