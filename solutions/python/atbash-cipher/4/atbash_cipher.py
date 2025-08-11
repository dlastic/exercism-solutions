import string
import textwrap

DEFAULT_GROUP_SIZE = 5
PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]
ATBASH_TABLE = str.maketrans(PLAIN, CIPHER)


def divide_into_groups(input_str: str, group_size: int) -> str:
    """Return string divided into groups of a specified number of characters."""
    return " ".join(textwrap.wrap(input_str, width=group_size))


def atbash_transform(text: str, group_output: bool = False) -> str:
    """Transform text using Atbash cipher (a↔z, b↔y, c↔x, etc.)"""
    cleaned = "".join(char for char in text if char.isalnum())
    transformed = cleaned.lower().translate(ATBASH_TABLE)

    return (
        divide_into_groups(transformed, DEFAULT_GROUP_SIZE)
        if group_output
        else transformed
    )


def encode(plain_text: str) -> str:
    """Return text encoded with the Atbash cipher."""
    return atbash_transform(plain_text, group_output=True)


def decode(ciphered_text: str) -> str:
    """Return text decoded with the Atbash cipher."""
    return atbash_transform(ciphered_text)
