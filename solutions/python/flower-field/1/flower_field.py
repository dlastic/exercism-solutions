EMPTY = " "
FLOWER = "*"


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
    new_garden = [list(row) for row in garden]

    def count_adjacent(row: int, col: int) -> int:
        """Count flowers adjacent to the given cell."""
        neighbors = [
            (i, j)
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            if (0 <= i < row_count and 0 <= j < col_count) and (i, j) != (row, col)
        ]
        return sum(garden[i][j] == FLOWER for i, j in neighbors)

    for r, row in enumerate(garden):
        for c, cell in enumerate(row):
            if cell == EMPTY:
                count = count_adjacent(r, c)
                if count:
                    new_garden[r][c] = str(count)

    return ["".join(row) for row in new_garden]
