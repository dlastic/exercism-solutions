import string

PLAIN_ALPHABET = string.ascii_lowercase
CIPHER_ALPHABET = PLAIN_ALPHABET[::-1]
ENCODE_MAP = dict(zip(PLAIN_ALPHABET, CIPHER_ALPHABET))
DEFAULT_GROUP_SIZE = 5


def divide_into_groups(input_str: str, group_size: int) -> str:
    """Return string divided into groups of a specified number of characters."""
    return " ".join(
        input_str[i : i + group_size] for i in range(0, len(input_str), group_size)
    )


def encode(plain_text: str) -> str:
    """Return text encoded with the Atbash cipher."""
    ciphered_text = []
    for char in plain_text.lower():
        if char.isalpha():
            ciphered_text.append(ENCODE_MAP[char])
        elif char.isdigit():
            ciphered_text.append(char)

    return divide_into_groups("".join(ciphered_text), DEFAULT_GROUP_SIZE)


def decode(ciphered_text: str) -> str:
    """Return text decoded with the Atbash cipher."""
    plain_text = []
    for char in ciphered_text:
        if char.isalpha():
            plain_text.append(ENCODE_MAP[char])
        elif char.isdigit():
            plain_text.append(char)

    return "".join(plain_text)
