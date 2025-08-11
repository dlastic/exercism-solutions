def answer(question: str) -> int:
    """Parse and evaluate simple math word problems."""
    OPERATOR_MAP = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "multiplied": lambda x, y: x * y,
        "divided": lambda x, y: x // y,
    }

    question_cleaned = question.removeprefix("What is").removesuffix("?").strip()
    tokens = question_cleaned.replace("by", "").split()

    if not tokens:
        raise ValueError("syntax error")
    if len(tokens) == 1:
        return int(tokens[0])
    if len(tokens) == 2 and tokens[1] not in OPERATOR_MAP:
        raise ValueError("unknown operation")

    try:
        remaining_tokens = tokens[:]
        while len(remaining_tokens) > 1:
            x, op, y, *rest = remaining_tokens
            result = OPERATOR_MAP[op](int(x), int(y))
            remaining_tokens = [result, *rest]
        return result
    except Exception:
        raise ValueError("syntax error")
