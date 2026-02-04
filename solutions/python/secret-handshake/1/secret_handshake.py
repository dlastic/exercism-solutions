ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> list[str]:
    """Return handshake actions decoded from a binary string."""
    if not set(binary_str) <= {"0", "1"}:
        raise ValueError("binary_str must contain only 0s and 1s")

    reverse_flag = binary_str[0] == "1"
    bits = binary_str[:0:-1]

    result = [action for bit, action in zip(bits, ACTIONS) if bit == "1"]

    return result[::-1] if reverse_flag else result
