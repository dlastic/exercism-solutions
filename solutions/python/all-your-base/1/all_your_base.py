def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert digits in one base into digits in another base."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if all(digit == 0 for digit in digits):
        return [0]

    # Convert to base-10
    decimal_value = 0
    for i, digit in enumerate(digits):
        decimal_value += digit * input_base ** (len(digits) - (i + 1))

    # Convert to output base
    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    output_digits.reverse()
    return output_digits
