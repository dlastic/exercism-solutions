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
    english_alph_ascii = set(range(ord("a"), ord("z") + 1))
    sentence_lower = sentence.lower()
    sentence_ascii = {ord(char) for char in sentence_lower}
    
    return english_alph_ascii.issubset(sentence_ascii)
