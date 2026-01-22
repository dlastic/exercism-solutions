import re
import string

def abbreviate(phrase: str) -> str:
    """Convert a phrase to its acronym."""
    pattern = f"[{re.escape(string.punctuation.replace('-', ''))}]"
    cleaned_phrase = re.sub(pattern, "", phrase)
    words = cleaned_phrase.replace("-", " ").split()

    return "".join(word[0].upper() for word in words)



