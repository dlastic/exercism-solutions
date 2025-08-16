EMPTY = " "
FLOWER = "*"
FLOWER_NUMERIC = -1
DIGITS = " 12345678"


def validate_board(board: list[str]) -> tuple[int, int]:
    """Check board validity and return its dimensions."""
    if not board:
        return 0, 0
    if len(board) == 1 and board[0] == "":
        return 1, 0

    row_count = len(board)
    col_count = len(board[0])
    for row in board:
        if len(row) != col_count or any(el not in [EMPTY, FLOWER] for el in row):
            raise ValueError("The board is invalid with current input.")
    return row_count, col_count


def annotate(garden: list[str]) -> list[str]:
    """Return a board where empty cells show the count of adjacent flowers."""
    row_count, col_count = validate_board(garden)
    if row_count == 0:
        return []
    if col_count == 0:
        return [""]
    new_garden = [[0] * col_count for _ in range(row_count)]
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    def increment_neighbors(row: int, col: int):
        """Notify all neighbors of this flower by incrementing their counts."""
        for dr, dc in neighbors:
            r, c = row + dr, col + dc
            if (
                0 <= r < row_count
                and 0 <= c < col_count
                and new_garden[r][c] != FLOWER_NUMERIC
            ):
                new_garden[r][c] += 1

    for r, row in enumerate(garden):
        for c, cell in enumerate(row):
            if cell == FLOWER:
                new_garden[r][c] = FLOWER_NUMERIC
                increment_neighbors(r, c)

    return [
        "".join(FLOWER if cell == FLOWER_NUMERIC else DIGITS[cell] for cell in row)
        for row in new_garden
    ]
