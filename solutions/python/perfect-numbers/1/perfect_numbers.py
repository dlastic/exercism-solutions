def classify(number: int) -> str:
    """ 
    Determine if a number is perfect, abundant, or deficient based on
    Nicomachus' (60 - 120 CE) classification scheme for positive integers.

    Args:
        number: Positive integer for class determination. 
        
    Returns:
        Classification of the number (perfect, abundant, deficient).
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i

    if number < aliquot_sum:
        return "abundant"
    if number > aliquot_sum:
        return "deficient"

    return "perfect"
