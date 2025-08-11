def equilateral(sides: list[int]) -> bool:
    """
    Return True if all sides are equal.

    A triangle is equilateral if all three sides have the same length.
    """
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    """
    Return True if at least two sides are equal.

    A triangle is isosceles if at least two of its sides are equal in length.
    """
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int]) -> bool:
    """
    Return True if all sides are different.

    A triangle is scalene if all three sides have different lengths.
    """
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides: list[int]) -> bool:
    """Return True if the sides can form a triangle.

    A valid triangle must satisfy the triangle inequality: the sum of any two sides
    must be greater than the length of the third side, and all sides must be positive.
    """
    a, b, c = sorted(sides)
    return a + b > c and a > 0