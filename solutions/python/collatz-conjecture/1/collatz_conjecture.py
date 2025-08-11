def steps(number: int) -> int:
    """
    Calculate the number of steps to reach 1 using the Collatz Conjecture.

    Starting with a positive integer `number`, repeatedly apply the following:
      - If the number is even, divide it by 2.
      - If the number is odd, multiply it by 3 and add 1.
    The process continues until the number reaches 1.
    """
    # Ensure the number is a positive integer
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    # Initialize step counter
    step = 0
    # Loop until number reaches 1, following the Collatz Conjecture rules
    while number > 1:
        number = number // 2 if number % 2 == 0 else 3 * number + 1
        step += 1

    return step
