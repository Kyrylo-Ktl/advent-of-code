from typing import override

from infrastructure.solutions.base import Solution

MOVE = tuple[str, int]


class Year2016Day1Part2Solution(Solution):

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
        """
        Time:  O(n*m)
        Space: O(n*m)

        Where n - number of moves,
              m - maximum steps per move
        """
        x = 0
        y = 0

        dx = 0
        dy = 1

        seen = {(x, y)}
        first_x_duplicate = None
        first_y_duplicate = None

        for direction, steps in moves:
            if first_x_duplicate is not None and first_y_duplicate is not None:
                break

            if direction == 'L':
                dx, dy = -dy, dx

            if direction == 'R':
                dx, dy = dy, -dx

            for _ in range(steps):
                x += dx
                y += dy

                if (x, y) in seen and first_x_duplicate is None and first_y_duplicate is None:
                    first_x_duplicate = x
                    first_y_duplicate = y
                    break

                seen.add((x, y))

        return abs(first_x_duplicate) + abs(first_y_duplicate)


if __name__ == '__main__':
    print(Year2016Day1Part2Solution.main())
