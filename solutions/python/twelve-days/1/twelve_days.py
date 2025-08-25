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


def build_verse(day: int) -> str:
    """Generate a verse for the given day."""
    day_gifts = [GIFTS[i] for i in range(day - 1, -1, -1)]
    if day > 1:
        day_gifts[-1] = "and " + day_gifts[-1]

    gifts_text = ", ".join(day_gifts)
    return (
        f"On the {ORDINALS[day - 1]} day of Christmas "
        f"my true love gave to me: {gifts_text}."
    )


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return verses for the Twelve Days of Christmas."""
    return [build_verse(i) for i in range(start_verse, end_verse + 1)]
