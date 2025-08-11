MAP = {"(": ")", "{": "}", "[": "]"}
OPENING_BRACKETS = ["(", "[", "{"]
CLOSING_BRACKETS = [")", "]", "}"]


def is_paired(input_string: str) -> bool:
    """Return True if all pairs of brackets, braces, and parentheses are matched"""
    bracket_stack = []

    for char in input_string:
        if char in OPENING_BRACKETS:
            bracket_stack.append(char)
        elif char in CLOSING_BRACKETS:
            if not bracket_stack or char != MAP[bracket_stack[-1]]:
                return False
            bracket_stack.pop()

    return not bracket_stack
