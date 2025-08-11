def equilateral(sides: list[int]) -> bool:
    """
    Check if a triangle is equilateral (all sides equal).
    
    Args:
        sides (list[int]): A list of three side lengths.
        
    Returns:
        bool: True if equilateral, False otherwise.
    """
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    """
    Check if a triangle is isosceles (at least two sides equal).
    
    Args:
        sides (list[int]): A list of three side lengths.
        
    Returns:
        bool: True if isosceles, False otherwise.
    """
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int]) -> bool:
    """
    Check if a triangle is scalene (all sides different).
    
    Args:
        sides (list[int]): A list of three side lengths.
        
    Returns:
        bool: True if scalene, False otherwise.
    """
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides: list[int]) -> bool:
    """
    Validate if sides can form a triangle.
    
    Args:
        sides (list[int]): A list of three side lengths.
        
    Returns:
        bool: True if valid triangle, False otherwise.
    """
    a, b, c = sorted(sides)
    return a + b > c and a > 0