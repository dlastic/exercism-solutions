COLOR_LIST = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

UNITS = [
    (1_000_000_000, "giga"),
    (1_000_000, "mega"),
    (1_000, "kilo"),
]

def label(colors: list[str]) -> str:
    """Convert a 3-band resistor color code to a resistance value."""
    base_value = 10 * COLOR_LIST[colors[0]] + COLOR_LIST[colors[1]]
    multiplier = 10 ** COLOR_LIST[colors[2]]
    resistance_ohms = base_value * multiplier
    
    for factor, name in UNITS:
        if resistance_ohms >= factor:
            value = resistance_ohms // factor
            return f"{value} {name}ohms"

    return f"{resistance_ohms} ohms"
