def equilateral(sides: list) -> bool:
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list) -> bool:
    return is_triangle(sides) and len(set(sides)) < 3


def scalene(sides: list) -> bool:
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides: list) -> bool:
    return sum(sides) - max(sides) >= max(sides) and min(sides) > 0