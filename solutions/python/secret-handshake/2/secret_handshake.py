ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str, actions: list[str] = ACTIONS) -> list[str]:
    """Return handshake actions decoded from a binary string."""
    if not set(binary_str) <= {"0", "1"}:
        raise ValueError("binary_str must contain only 0s and 1s")

    value = int(binary_str, 2)
    result = [
        action
        for i, action in enumerate(actions)
        if value & (1 << i)
    ]  # fmt: skip

    if value & (1 << len(actions)):
        result.reverse()

    return result
