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
    # # Calculate the distance from the center (0, 0) to the point (x, y)
    coordinate_radius = (x ** 2 + y ** 2) ** 0.5
    
    # Determine points scored based on the coordinate radius
    for target_radius, points in TARGET_RADIUS_POINTS.items():
        if coordinate_radius <= target_radius:
            return points
    
    # Return 0 if the dart lands outside the target
    return 0
