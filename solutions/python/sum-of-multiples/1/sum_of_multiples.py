def sum_of_multiples(limit: int, base_values: list[int]) -> int:
    """Return sum of unique multiples of base values below the limit."""
    return sum(
        {
            multiple
            for value in base_values
            if value != 0
            for multiple in range(value, limit, value)
        }
    )
