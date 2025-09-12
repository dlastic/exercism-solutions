NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"


class Robot:
    """A simple robot on a 2D grid that can move and rotate."""

    DIRECTIONS: tuple[str, ...] = (NORTH, EAST, SOUTH, WEST)
    MOVEMENT_VECTORS: dict[str, tuple[int, int]] = {
        NORTH: (0, 1),
        EAST: (1, 0),
        SOUTH: (0, -1),
        WEST: (-1, 0),
    }
    _ACTIONS: dict[str, str] = {
        "R": "_turn_right",
        "L": "_turn_left",
        "A": "_advance",
    }

    def __init__(self, direction: str = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        if direction not in self.DIRECTIONS:
            raise ValueError(f"Invalid direction: {direction}")
        self.x = x_pos
        self.y = y_pos
        self._dir_idx = self.DIRECTIONS.index(direction)

    @property
    def direction(self) -> str:
        """Return the robot's current direction."""
        return self.DIRECTIONS[self._dir_idx]

    @property
    def coordinates(self) -> tuple[int, int]:
        """Return the robot's (x, y) position."""
        return (self.x, self.y)

    def move(self, instructions: str) -> None:
        """Execute a string of instructions ('R', 'L', 'A').

        Instructions are case-insensitive.
        """
        for instruction in instructions.upper():
            if instruction not in self._ACTIONS:
                raise ValueError(f"Invalid instruction: {instruction}")
            getattr(self, self._ACTIONS[instruction])()

    def _turn_right(self) -> None:
        self._dir_idx = (self._dir_idx + 1) % 4

    def _turn_left(self) -> None:
        self._dir_idx = (self._dir_idx - 1) % 4

    def _advance(self) -> None:
        dx, dy = self.MOVEMENT_VECTORS[self.direction]
        self.x += dx
        self.y += dy
