import string


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
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
        
    encoding_table = str.maketrans(
        lower_case + upper_case,
        lower_case[key % 26:] + lower_case[:key % 26] +
        upper_case[key % 26:] + upper_case[:key % 26]
    )

    return text.translate(encoding_table)
