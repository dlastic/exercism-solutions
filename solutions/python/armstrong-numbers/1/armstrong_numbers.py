def is_armstrong_number(number: int) -> bool:
    """
    Return True if a number is an Armstrong number.
    
    An Armstrong number is a number that is the sum of its own digits each 
    raised to the power of the number of digits.
    """
    num_digits = len(str(number))
    return number == sum(int(digit) ** num_digits for digit in str(number))
