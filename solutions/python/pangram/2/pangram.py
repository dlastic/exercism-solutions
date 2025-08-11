import string


def is_pangram(sentence: str) -> bool:
    """
    Check if the given sentence is a pangram. A pangram is
    a sentence that contains every letter of the English
    alphabet at least once.

    Args:
        sentence: The sentence to check.

    Returns:
        True if the sentence is a pangram, False otherwise.
    """
    sentence_lowercase_set = set(sentence.lower())
    ascii_lowercase_set = set(string.ascii_lowercase)
    
    return ascii_lowercase_set.issubset(sentence_lowercase_set)
