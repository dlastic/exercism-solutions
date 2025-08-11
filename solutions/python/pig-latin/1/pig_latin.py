VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def translate(text: str) -> str:
    """Translate English text to Pig Latin""" 
    words = text.split()
    pig_latin_words = []

    for word in words:
        # Rule 1
        if word[0] in VOWELS or word.startswith("xr") or word.startswith("yt"):
            pig_latin_words.append(word + "ay")
            continue

        # Rules 2 - 4
        leading_consonant_count = 0
        for char in word:
            if char in CONSONANTS:
                leading_consonant_count += 1
            else:
                break
        if leading_consonant_count > 0:
            # Rule 3
            if word[leading_consonant_count - 1:].startswith("qu"):
                pig_latin_word = word[leading_consonant_count + 1:] + word[:leading_consonant_count + 1] + "ay"
            # Rule 4
            elif "y" in word[1:leading_consonant_count]:
                slice_index = word[1:leading_consonant_count].find("y") + 1
                pig_latin_word = word[slice_index:] + word[:slice_index] + "ay"
            # Rule 2
            else:
                pig_latin_word = word[leading_consonant_count:] + word[:leading_consonant_count] + "ay"
            pig_latin_words.append(pig_latin_word)

    return " ".join(pig_latin_words)