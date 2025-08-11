DEFAULT_GROUP_SIZE = 5


def divide_into_groups(input_str: str, group_size: int) -> str:
    """Return string divided into groups of a specified number of characters."""
    return " ".join(
        input_str[i : i + group_size] for i in range(0, len(input_str), group_size)
    )


def atbash_transform(text: str, group_output: bool = False) -> str:
    """Transform text using Atbash cipher (a↔z, b↔y, c↔x, etc.)"""
    result = [
        chr(ord("z") - (ord(char) - ord("a"))) if char.isalpha() else char
        for char in text.lower()
        if char.isalnum()
    ]
    transformed = "".join(result)

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
