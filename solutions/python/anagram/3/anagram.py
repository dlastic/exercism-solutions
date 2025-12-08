from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Return a list of candidates that are anagrams of the given word."""
    word_lower = word.lower()
    word_count = Counter(word_lower)

    return [
        candidate
        for candidate in candidates
        if (candidate_lower := candidate.lower()) != word_lower
        and Counter(candidate_lower) == word_count
    ]
