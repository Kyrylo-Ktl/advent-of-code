from itertools import groupby
from sys import maxsize
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day12Part2Solution(Solution):
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
        Time:  O(n*m*min(n,m))
        Space: O(n*m)

        Where n - number of rows in garden,
              m - number of columns in garden
        """
        total_price = 0
        processed = set()

        for x, row in enumerate(garden):
            for y, plant in enumerate(row):
                # Already processed
                if (x, y) in processed:
                    continue

                # Retrieving connected plants region
                plants_region = cls.get_plants_region(garden, plant_x=x, plant_y=y)

                # Marking region members as processed
                processed |= plants_region

                # Calculating region price
                region_size = len(plants_region)
                region_sides = cls.get_region_sides(plants_region)
                region_price = region_size * region_sides

                total_price += region_price

        return total_price

    @classmethod
    def get_plants_region(cls, garden: list[list[str]], plant_x: int, plant_y: int) -> set[tuple[int, int]]:
        n = len(garden)
        m = len(garden[0])

        region = set()
        queue = [(plant_x, plant_y)]

        while queue:
            x, y = queue.pop()

            # Already processed
            if (x, y) in region:
                continue

            # Marking as processed
            region.add((x, y))

            for dx, dy in cls.MOVES:
                nx, ny = x + dx, y + dy

                # Out of garden bounds
                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                # Another plant or empty cell
                if garden[nx][ny] != garden[plant_x][plant_y]:
                    continue

                queue.append((nx, ny))

        return region

    @classmethod
    def get_region_sides(cls, region: set[tuple[int, int]]) -> int:
        min_row, max_row, min_col, max_col = cls.get_region_bounds(region)

        total_rows = max_row - min_row + 1
        total_cols = max_col - min_col + 1

        sides = 0

        # Counting "down" sides in region
        for row in range(min_row, max_row + 1):
            is_down_side = [False] * total_cols

            for col in range(min_col, max_col + 1):
                if (row, col) in region and (row - 1, col) not in region:
                    is_down_side[col - min_col] = True

            # Counting sides with ignoring continuous values
            for is_side, _ in groupby(is_down_side):
                if is_side:
                    sides += 1

        # Counting "top" sides in region
        for row in range(min_row, max_row + 1):
            is_top_side = [False] * total_cols

            for col in range(min_col, max_col + 1):
                if (row, col) in region and (row + 1, col) not in region:
                    is_top_side[col - min_col] = True

            # Counting sides with ignoring continuous values
            for is_side, _ in groupby(is_top_side):
                if is_side:
                    sides += 1

        # Counting "left" sides in region
        for col in range(min_col, max_col + 1):
            is_left_side = [False] * total_rows

            for row in range(min_row, max_row + 1):
                if (row, col) in region and (row, col - 1) not in region:
                    is_left_side[row - min_row] = True

            # Counting sides with ignoring continuous values
            for is_side, _ in groupby(is_left_side):
                if is_side:
                    sides += 1

        # Counting "right" sides in region
        for col in range(min_col, max_col + 1):
            is_right_side = [False] * total_rows

            for row in range(min_row, max_row + 1):
                if (row, col) in region and (row, col + 1) not in region:
                    is_right_side[row - min_row] = True

            # Counting sides with ignoring continuous values
            for is_side, _ in groupby(is_right_side):
                if is_side:
                    sides += 1

        return sides

    @classmethod
    def get_region_bounds(cls, plants: set[tuple[int, int]]) -> tuple[int, int, int, int]:
        min_row = maxsize
        min_col = maxsize

        max_row = -maxsize
        max_col = -maxsize

        for row, col in plants:
            min_col = min(min_col, col)
            min_row = min(min_row, row)

            max_col = max(max_col, col)
            max_row = max(max_row, row)

        return min_row, max_row, min_col, max_col


if __name__ == '__main__':
    print(Year2024Day12Part2Solution.main())
