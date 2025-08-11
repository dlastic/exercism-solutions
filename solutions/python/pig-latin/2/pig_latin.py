VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def translate(text: str) -> str:
    """Translate English text to Pig Latin."""

    def pig_latin_word(word):
        # Rule 1: Starts with vowel sound
        if word[0] in VOWELS or word.startswith("xr") or word.startswith("yt"):
            return word + "ay"

        # Rule 3: Consonant cluster ends with 'qu'
        if word.startswith("qu"):
            return word[2:] + "quay"

        for i, char in enumerate(word):
            # Rule 4: 'y' as a vowel (not at start)
            if char in VOWELS or (char == "y" and i != 0):
                # Special handling for 'qu' after consonant(s)
                if word[i - 1:i + 1] == "qu":
                    return word[i + 1:] + word[:i + 1] + "ay"
                return word[i:] + word[:i] + "ay"

        return word + "ay"  # fallback (shouldn't happen for valid input)

    return " ".join(pig_latin_word(word) for word in text.split())
