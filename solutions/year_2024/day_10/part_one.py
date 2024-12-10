from collections.abc import Iterable
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day10Part1Solution(Solution):
    MOVES = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    )

    MIN_HEIGHT = 0
    MAX_HEIGHT = 9

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[int]]]:
        matrix = []

        for line in text_input.split('\n'):
            matrix.append([int(height) for height in line])

        return {'matrix': matrix}

    @classmethod
    @override
    def solve(cls, matrix: list[list[int]]) -> int:
        """
        Time:  O(n*m*k^2)
        Space: O(k)

        Where n - number of topographic map rows
              m - number of topographic map columns
              k - maximum hiking trail length (10 in this case)
        """
        n = len(matrix)
        m = len(matrix[0])

        def get_reachable_peaks(x: int, y: int) -> Iterable[tuple[int, int]]:
            if matrix[x][y] == cls.MAX_HEIGHT:
                yield x, y

            for dx, dy in cls.MOVES:
                next_x, next_y = x + dx, y + dy

                # Neighbor cell out of topographic map bounds
                if not (0 <= next_x < n and 0 <= next_y < m):
                    continue

                # Neighbor cell must be one unit higher
                if matrix[x][y] + 1 != matrix[next_x][next_y]:
                    continue

                yield from get_reachable_peaks(next_x, next_y)

        score = 0

        for i, row in enumerate(matrix):
            for j, height in enumerate(row):
                if height == cls.MIN_HEIGHT:
                    uniq_peaks = set(get_reachable_peaks(i, j))
                    score += len(uniq_peaks)

        return score


if __name__ == '__main__':
    print(Year2024Day10Part1Solution.main())
