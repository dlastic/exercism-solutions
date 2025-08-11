def equilateral(sides: list[int]) -> bool:
    """Return True if the triangle is equilateral (all sides are equal)."""
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    """Return True if the triangle is isosceles (at least two sides are equal)."""
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int]) -> bool:
    """Return True if the triangle is scalene (all sides are different)."""
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides: list[int]) -> bool:
    """Return True if the sides can form a valid triangle."""
    a, b, c = sorted(sides)
    return a + b > c and a > 0