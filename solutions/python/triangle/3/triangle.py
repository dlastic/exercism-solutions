def equilateral(sides: list[int]) -> bool:
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int]) -> bool:
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides: list[int]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c and a > 0