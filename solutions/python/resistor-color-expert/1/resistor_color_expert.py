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

TOLERANCE_LIST = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

UNITS = [
    (1_000_000_000, "giga"),
    (1_000_000, "mega"),
    (1_000, "kilo"),
]


def resistor_label(colors: list[str]) -> str:
    """Convert a resistor color code to a resistance value.

    One band resistors only have the color black, representing 0 ohms.
    4 and 5 band resistors have tolerance values represented by the last band.
    """
    if len(colors) == 1:
        return "0 ohms"

    base_value = 0
    for color in colors[:-2]:
        base_value = base_value * 10 + COLOR_LIST[color]
    multiplier = 10 ** COLOR_LIST[colors[-2]]
    resistance_ohms = base_value * multiplier
    tolerance = f" ±{TOLERANCE_LIST[colors[-1]]}%"

    for factor, name in UNITS:
        if resistance_ohms >= factor:
            value = resistance_ohms / factor
            if value.is_integer():
                value = int(value)
            return f"{value} {name}ohms{tolerance}"

    return f"{resistance_ohms} ohms{tolerance}"
