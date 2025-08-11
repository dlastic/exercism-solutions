def answer(question: str) -> int:
    """Parse and evaluate simple math word problems."""
    OPERATOR_MAP = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "multiplied": lambda x, y: x * y,
        "divided": lambda x, y: x // y,
    }

    question_cleaned = question.removeprefix("What is").removesuffix("?").strip()
    equation_parts = question_cleaned.replace("by", "").split()

    if not equation_parts:
        raise ValueError("syntax error")
    if len(equation_parts) == 1:
        return int(equation_parts[0])
    if len(equation_parts) == 2 and equation_parts[1] not in OPERATOR_MAP:
        raise ValueError("unknown operation")

    try:
        while len(equation_parts) > 1:
            x, op, y, *rest = equation_parts
            result = OPERATOR_MAP[op](int(x), int(y))
            equation_parts = [result, *rest]

        return result
    except Exception:
        raise ValueError("syntax error")
