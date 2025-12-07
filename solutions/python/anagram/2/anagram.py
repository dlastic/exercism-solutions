from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Return a list of candidates that are anagrams of the given word."""
    word_lower = word.lower()
    word_count = Counter(word_lower)
    result = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower != word_lower and Counter(candidate_lower) == word_count:
            result.append(candidate)

    return result
