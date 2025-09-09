NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"


class Robot:
    """A simple robot on a 2D grid that can move and rotate."""

    DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
    MOVEMENT_VECTORS = {NORTH: (0, 1), EAST: (1, 0), SOUTH: (0, -1), WEST: (-1, 0)}

    def __init__(self, direction: str = NORTH, x_pos: int = 0, y_pos: int = 0):
        if direction not in self.DIRECTIONS:
            raise ValueError(f"Invalid direction: {direction}")
        if not isinstance(x_pos, int) or not isinstance(y_pos, int):
            raise ValueError("Coordinates must be integers.")
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
        self._actions = {
            "R": self._turn_right,
            "L": self._turn_left,
            "A": self._advance,
        }
        self._dir_idx = self.DIRECTIONS.index(direction)

    @property
    def coordinates(self) -> tuple[int, int]:
        """Return the robot's (x, y) position."""
        return (self.x, self.y)

    def move(self, instructions: str) -> None:
        """Execute a string of instructions ('R', 'L', 'A')."""
        for instruction in instructions.upper():
            if instruction not in self._actions:
                raise ValueError(f"Invalid instruction: {instruction}")
            self._actions[instruction]()

    def _turn_right(self) -> None:
        self._dir_idx = (self._dir_idx + 1) % 4
        self.direction = self.DIRECTIONS[self._dir_idx]

    def _turn_left(self) -> None:
        self._dir_idx = (self._dir_idx - 1) % 4
        self.direction = self.DIRECTIONS[self._dir_idx]

    def _advance(self) -> None:
        dx, dy = self.MOVEMENT_VECTORS[self.direction]
        self.x += dx
        self.y += dy
