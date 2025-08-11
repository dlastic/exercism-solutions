# Map the target radius to corresponding points scored
TARGET_RADIUS_POINTS = {1: 10, 5: 5, 10: 1}

def score(x: float, y: float) -> int:
    """
    Calculate the score based on the dart's position.

    Args:
        x: The x-coordinate of the dart's landing position.
        y: The y-coordinate of the dart's landing position.

    Returns:
        Points scored based on the dart's distance from the center.
    """
    coordinate_radius = (x ** 2 + y ** 2) ** 0.5
    result = filter(lambda item: coordinate_radius <= item[0], TARGET_RADIUS_POINTS.items())
    
    return next(result, (None, 0))[1]
