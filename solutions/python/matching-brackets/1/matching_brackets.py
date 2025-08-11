MAP = {"(": ")", "{": "}", "[": "]", ")": "0", "}": "0", "]": "0"}
BRACKETS = ["(", "{", "[", ")", "}", "]"]


def is_paired(input_string: str) -> bool:
    """Return True if all pairs of brackets, braces, and parentheses are matched"""

    brackets_found = [char for char in input_string if char in BRACKETS]
    bracket_count = len(brackets_found)

    for _ in range(bracket_count // 2):
        for i, bracket in enumerate(brackets_found[:-1]):
            if brackets_found[i + 1] == MAP[bracket]:
                brackets_found.pop(i + 1)
                brackets_found.pop(i)
                break

    return not brackets_found
