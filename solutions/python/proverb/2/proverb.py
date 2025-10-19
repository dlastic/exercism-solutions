def proverb(*items: str, qualifier: str | None = None) -> list[str]:
    """Return proverb lines for given items and optional qualifier."""
    if not items:
        return []

    lines = [
        f"For want of a {a} the {b} was lost."
        for a, b
        in zip(items, items[1:])
    ]
    lines.append(
        f"And all for the want of a {(qualifier + ' ') if qualifier else ''}{items[0]}."
    )
    return lines
