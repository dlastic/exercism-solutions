def square_root(number: int) -> int | None:
    """
    Return the integer square root of a perfect square, 
    or None if not a perfect square.
    """
    low, high = 1, number
    
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == number:
            return mid
        if mid * mid < number:
            low = mid + 1
        else:
            high = mid - 1

    return None
