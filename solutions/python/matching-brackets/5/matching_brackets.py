MAP = {"(": ")", "{": "}", "[": "]"}
OPENING_BRACKETS = ["(", "[", "{"]
CLOSING_BRACKETS = [")", "]", "}"]


def is_paired(input_string: str) -> bool:
    """Return True if all pairs of brackets are matched"""
    bracket_stack = []

    for char in input_string:
        if char in OPENING_BRACKETS:
            bracket_stack.append(char)
        elif char in CLOSING_BRACKETS:
            try:
                if MAP[bracket_stack.pop()] != char:
                    return False
            except IndexError:
                return False

    return not bracket_stack 
