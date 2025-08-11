def is_valid(isbn: str) -> bool:
    """
    Validate an ISBN-10 number.
    
    Args:
        isbn: The ISBN number as a string.
    
    Returns:
        True if valid, False otherwise.
    """
    isbn_list = list(isbn.replace("-", ""))

    if len(isbn_list) != 10:
        return False
    if isbn_list[-1] == "X":
        isbn_list[-1] = "10"

    try:
        isbn_digits = [int(i) for i in isbn_list]
    except ValueError:
        return False
        
    isbn_sum = sum((10 - i) * digit for i, digit in enumerate(isbn_digits))

    return isbn_sum % 11 == 0
        