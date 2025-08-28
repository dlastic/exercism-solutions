TOTAL_DAYS = 12

ORDINALS = (
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
)
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

    Args:
        start_verse: Starting day (1-12).
        end_verse: Ending day (1-12).

    Returns:
        A list of verse strings. If start_verse > end_verse, an empty
        list is returned.

    Raises:
        ValueError: If start_verse or end_verse is out of range.
    """
    if not (1 <= start_verse <= TOTAL_DAYS) or not (1 <= end_verse <= TOTAL_DAYS):
        raise ValueError(f"Start and end verses must be between 1 and {TOTAL_DAYS}.")

    return [build_verse(i) for i in range(start_verse, end_verse + 1)]
