def is_isogram(string: str) -> bool:
    """
    Check if a word or phrase is an isogram (no repeating letters).

    Args:
        string: The input word or phrase.

    Returns:
        True if the input is an isogram, False otherwise.
    """
    clean_string = string.replace("-", "").replace(" ", "").lower()

    return len(clean_string) == len(set(clean_string))
