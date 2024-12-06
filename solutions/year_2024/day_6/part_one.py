from dataclasses import dataclass
from enum import StrEnum
from typing import override, Self

from dotenv.parser import Position

from infrastructure.solutions.base import Solution


class Symbol(StrEnum):
    GUARD = '^'
    WALL = '#'
    CELL = '.'


@dataclass
class Direction:
    dx: int
    dy: int

    def turn_right(self) -> Self:
        return Direction(self.dy, -self.dx)


@dataclass
class Position:
    x: int
    y: int

    def __eq__(self, other: Self):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def move(self, direction: Direction) -> Self:
        return Position(self.x + direction.dx, self.y + direction.dy)


@dataclass
class Guard:
    direction: Direction
    position: Position

    def move_forward(self) -> Self:
        return Guard(
            position=self.position.move(self.direction),
            direction=self.direction,
        )

    def turn_right(self) -> Self:
        return Guard(
            position=self.position,
            direction=self.direction.turn_right(),
        )


class Year2024Day6Part1Solution(Solution):
    # Direction upwards according to the guard symbol
    INITIAL_DIRECTION = Direction(dx=-1, dy=0)

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[str]]]:
        positions = []

        for line in text_input.split('\n'):
            positions.append(list(line))

        return {'positions': positions}

    @classmethod
    @override
    def solve(cls, positions: list[list[str]]) -> int:
        """
        Time:  O(n*m)
        Space: O(n*m)

        Where n - number of lines in positions,
              m - number of columns in positions
        """
        n = len(positions)
        m = len(positions[0])

        curr_guard = Guard(
            position=cls.get_guard_position(positions),
            direction=cls.INITIAL_DIRECTION,
        )

        # Visited cells
        visited = set()

        while True:
            visited.add(curr_guard.position)

            # To track where the guard will be when he moves forward
            next_guard = curr_guard.move_forward()

            # The guard will be off the map when moving forward
            if not (0 <= next_guard.position.x < n and 0 <= next_guard.position.y < m):
                break

            # The guard will bump into the wall when moving forward, just turn right
            if positions[next_guard.position.x][next_guard.position.y] == Symbol.WALL:
                next_guard = curr_guard.turn_right()

            curr_guard = next_guard

        return len(visited)

    @classmethod
    def get_guard_position(cls, positions: list[list[str]]) -> Position:
        # To be off the map immediately in case of no guards
        position = Position(x=-1, y=-1)

        for i, line in enumerate(positions):
            for j, char in enumerate(line):
                if char == Symbol.GUARD:
                    position.x = i
                    position.y = j

        return position


if __name__ == '__main__':
    print(Year2024Day6Part1Solution.main())
