def rotate(text: str, key: int) -> str:
    """
    Encrypt text using a Caesar cipher with the given key.

    Shifts each letter by 'key' positions while preserving case.
    Non-alphabetic characters remain unchanged.

    Args:
        text: The input text.
        key: The shift value.

    Returns:
        The encrypted text.
    """
    cipher_text = ""

    for char in text:
        if char.isupper():
            cipher_text += chr((ord(char) - ord("A") + key) % 26 + ord("A"))
        elif char.islower():
            cipher_text += chr((ord(char) - ord("a") + key) % 26 + ord("a"))
        else:
            cipher_text += char

    return cipher_text
