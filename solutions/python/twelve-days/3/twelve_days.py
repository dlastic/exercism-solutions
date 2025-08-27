ORDINALS = (
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
)
TOTAL_DAYS = 12

GIFTS = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)

VERSE_TEMPLATE = (
    "On the {ordinal} day of Christmas "
    "my true love gave to me: {gifts}."
)


def build_verse(day: int) -> str:
    """Generate a verse for the given day.

    Args:
        day: Day number (1-12) of Christmas.

    Returns:
        A string containing the verse for the given day.
    """
    if not (1 <= day <= TOTAL_DAYS):
        raise ValueError(f"Day must be between 1 and {TOTAL_DAYS}.")

    day_gifts = [GIFTS[i] for i in range(day - 1, -1, -1)]
    if day > 1:
        day_gifts[-1] = "and " + day_gifts[-1]

    gifts_text = ", ".join(day_gifts)
    return VERSE_TEMPLATE.format(
        ordinal=ORDINALS[day - 1],
        gifts=gifts_text
    )


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return verses for the Twelve Days of Christmas.

    If start_verse > end_verse, an empty list is returned.
    """
    if not (1 <= start_verse <= TOTAL_DAYS) or not (1 <= end_verse <= TOTAL_DAYS):
        raise ValueError(f"Start and end verses must be between 1 and {TOTAL_DAYS}.")

    return [build_verse(i) for i in range(start_verse, end_verse + 1)]
