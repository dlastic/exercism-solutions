def spiral_matrix(size: int) -> list[list[int]]:
    """Return a square matrix of a given size in a clockwise spiral form."""
    if size == 0:
        return []

    matrix = [[0] * size for _ in range(size)]
    num = 1
    top, bottom = 0, size - 1
    left, right = 0, size - 1

    while top <= bottom and left <= right:
        # left -> right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # top -> bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # right -> left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # bottom -> top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix
