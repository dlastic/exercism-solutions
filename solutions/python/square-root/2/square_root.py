def square_root(number: int) -> int | None:
    """
    Return the integer square root of a perfect square, 
    or None if not a perfect square.
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Only positive integers are allowed")
    
    start, end = 1, number
    while start <= end:
        guess = (start + end) // 2
        if guess * guess == number:
            return guess
        if guess * guess < number:
            start = guess + 1
        else:
            end = guess - 1

    return None
