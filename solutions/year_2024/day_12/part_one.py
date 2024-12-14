from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day12Part1Solution(Solution):
    MOVES = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    )

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[str]]]:
        garden = []

        for line in text_input.split('\n'):
            garden.append(list(line))

        return {'garden': garden}

    @classmethod
    @override
    def solve(cls, garden: list[list[str]]) -> int:
        """
        Time:  O(n*m)
        Space: O(n*m)

        Where n - number of rows in garden,
              m - number of columns in garden
        """
        n = len(garden)
        m = len(garden[0])

        visited = set()

        def dfs(i: int, j: int, plant: str) -> tuple[int, int]:
            # Zero area, one perimeter side
            if not (0 <= i < n and 0 <= j < m):
                return 0, 1

            # Zero area, one perimeter side
            if garden[i][j] != plant:
                return 0, 1

            # Already processed
            if (i, j) in visited:
                return 0, 0

            visited.add((i, j))

            area = 1
            perimeter = 0

            for di, dj in cls.MOVES:
                next_i, next_j = i + di, j + dj

                next_area, next_perimeter = dfs(next_i, next_j, plant)

                area += next_area
                perimeter += next_perimeter

            return area, perimeter

        total_price = 0

        for i, row in enumerate(garden):
            for j, plant in enumerate(row):
                area, perimeter = dfs(i, j, plant)
                total_price += area * perimeter

        return total_price


if __name__ == '__main__':
    print(Year2024Day12Part1Solution.main())
