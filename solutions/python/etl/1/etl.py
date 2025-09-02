def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """
    Transform legacy points-to-letters data
    into a direct letter-to-points mapping.

    Example:
        Input:
            {1: ["A", "E", "I", "O", "U", "L"],
             2: ["D", "G"],
             3: ["B", "C", "M", "P"]}
        Output:
            {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1,
             "d": 2, "g": 2, "b": 3, "c": 3, "m": 3, "p": 3}

    Args:
        legacy_data: Mapping of point values to lists of uppercase letters.

    Returns:
        Mapping of each lowercase letter to its point value.
    """
    return {
        letter.lower(): points
        for points, letters in legacy_data.items()
        for letter in letters
    }
    