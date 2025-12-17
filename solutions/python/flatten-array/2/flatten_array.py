from typing import Generator


def generate_flattened(iterable: list) -> Generator:
    """Generate values from a nested list skipping None values."""
    for item in iterable:
        if isinstance(item, list):
            yield from generate_flattened(item)
        elif item is not None:
            yield item


def flatten(iterable: list) -> list:
    """Return a flattened list from a nested list."""
    return list(generate_flattened(iterable))
