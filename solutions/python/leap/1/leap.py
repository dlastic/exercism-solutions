def leap_year(year):
    if divisible_by_400(year): return True
    if divisible_by_4(year) and not divisible_by_100(year): return True
    return False


def divisible_by_4(year):
    return year % 4 == 0


def divisible_by_100(year):
    return year % 100 == 0


def divisible_by_400(year):
    return year % 400 == 0