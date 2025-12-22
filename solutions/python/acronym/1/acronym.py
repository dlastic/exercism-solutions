import re
import string

def abbreviate(phrase: str) -> str:
    """Convert a phrase to its acronym."""
    pattern = f"[{re.escape(string.punctuation.replace('-', ''))}]"
    cleaned_phrase = re.sub(pattern, "", phrase)
    words = cleaned_phrase.replace("-", " ").upper().split()

    return "".join(word[0] for word in words)



