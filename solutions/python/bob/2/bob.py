def response(hey_bob: str) -> str:
    """
    Determine Bob's response to various types of statements or questions.
    
    Bob responds differently depending on the input:
      - Yelled question (all uppercase with a question mark): "Calm down, I know what I'm doing!"
      - Regular question (ends with a question mark): "Sure."
      - Yelling (all uppercase): "Whoa, chill out!"
      - Silence (empty or whitespace): "Fine. Be that way!"
      - Other statements: "Whatever."

    Args:
        hey_bob: The statement or question directed at Bob.
    Returns:
        Bob's response based on the input type.
    """
    hey_bob_stripped = hey_bob.strip()

    # Check if the input is a question (with or without yelling)
    if hey_bob_stripped.endswith("?"):
        if hey_bob_stripped.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."

    # Check if the input is yelling
    if hey_bob_stripped.isupper():
        return "Whoa, chill out!"

    # Check if the input is silence
    if not hey_bob_stripped:
        return "Fine. Be that way!"

    # Default response to other statements
    return "Whatever."
