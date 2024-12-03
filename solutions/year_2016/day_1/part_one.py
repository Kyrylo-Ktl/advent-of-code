from typing import override

from infrastructure.solutions.base import Solution

MOVE = tuple[str, int]


class Year2016Day1Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[MOVE]]:
        moves = []

        for line in text_input.split(', '):
            # R2 or L43 formats
            direction = line[0]
            steps = int(line[1:])

            moves.append((direction, int(steps)))

        return {'moves': moves}

    @classmethod
    @override
    def solve(cls, moves: list[MOVE]) -> int:
        x = 0
        y = 0

        dx = 0
        dy = 1

        for direction, steps in moves:
            if direction == 'L':
                dx, dy = -dy, dx

            if direction == 'R':
                dx, dy = dy, -dx

            x += dx * steps
            y += dy * steps

        return abs(x) + abs(y)


if __name__ == '__main__':
    print(Year2016Day1Part1Solution.main())
