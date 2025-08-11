def square_root(number: int) -> int:
    """Return the square root of a perfect square."""
    if not isinstance(number, int) or number < 1:
        raise ValueError("Only positive integers are allowed")
    
    start, end = 1, number
    while start <= end:
        guess = (start + end) // 2
        guess_squared = guess * guess
        if guess_squared == number:
            return guess
        if guess_squared < number:
            start = guess + 1
        else:
            end = guess - 1

    return ValueError(f"{number} is not a perfect square")