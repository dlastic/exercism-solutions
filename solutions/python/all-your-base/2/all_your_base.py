def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert digits in one base into digits in another base."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if not sum(digits):
        return [0]

    # Convert to base-10
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * input_base + digit

    # Convert to output base
    output_digits = []
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, output_base)
        output_digits.append(remainder)

    output_digits.reverse()
    return output_digits
