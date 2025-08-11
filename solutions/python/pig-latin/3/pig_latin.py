VOWELS = "aeiou"
VOWELS_Y = "aeiouy"
SPECIALS = ("xr", "yt")

def translate(text: str) -> str:
    """Translate English text (sentence) to Pig Latin."""

    def translate_word(word: str) -> str:
        """Translate a word to Pig Latin"""

        # Rule 1: Starts with a vowel, or with "xr"/"yt"
        if word[0] in VOWELS or word[:2] in SPECIALS:
            return word + "ay"

        # Rule 3a: Zero consonants followed by "qu"
        if word.startswith("qu"):
            return word[2:] + "quay"

        for i, char in enumerate(word):
            # Rule 2 & 4: Consonant cluster followed by vowel or "y"
            if char in VOWELS_Y and i != 0:
                # Rule 3b: Consonant cluster followed by "qu"
                if char == "u" and word[i - 1] == "q":
                    return word[i + 1:] + word[:i + 1] + "ay"
                return word[i:] + word[:i] + "ay"

        # Fallback if word doesn't follow any rule
        return word

    return " ".join(translate_word(word) for word in text.split())