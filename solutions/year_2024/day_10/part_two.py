from functools import cache
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day10Part2Solution(Solution):
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
        Time:  O(n*m)
        Space: O(n*m)

        Where n - number of topographic map rows
              m - number of topographic map columns
              k - maximum hiking trail length (10 in this case)
        """
        n = len(matrix)
        m = len(matrix[0])

        @cache
        def get_reachable_peaks(x: int, y: int) -> int:
            reachable = 0

            if matrix[x][y] == cls.MAX_HEIGHT:
                reachable += 1

            for dx, dy in cls.MOVES:
                next_x, next_y = x + dx, y + dy

                # Neighbor cell out of topographic map bounds
                if not (0 <= next_x < n and 0 <= next_y < m):
                    continue

                # Neighbor cell must be one unit higher
                if matrix[x][y] + 1 != matrix[next_x][next_y]:
                    continue

                reachable += get_reachable_peaks(next_x, next_y)

            return reachable

        rating = 0

        for i, row in enumerate(matrix):
            for j, height in enumerate(row):
                if height == cls.MIN_HEIGHT:
                    rating += get_reachable_peaks(i, j)

        return rating


if __name__ == '__main__':
    print(Year2024Day10Part2Solution.main())
