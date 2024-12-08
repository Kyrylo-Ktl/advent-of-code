from collections import defaultdict
from enum import StrEnum
from itertools import combinations
from typing import Iterable, override

from infrastructure.solutions.base import Solution

Position = tuple[int, int]


class Cell(StrEnum):
    EMPTY = '.'
    ANTINODE = '#'


class Year2024Day8Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[str]]]:
        antennas_map = []

        for line in text_input.split('\n'):
            antennas_map.append(list(line))

        return {'antennas_map': antennas_map}

    @classmethod
    @override
    def solve(cls, antennas_map: list[list[str]]) -> int:
        """
        Time:  O(n^2*m^2*max(n,m))
        Space: O(n*m)

        Where n - number of rows in antennas map,
              m - number of columns in antennas map
        """
        n = len(antennas_map)
        m = len(antennas_map[0])

        # To group antennas with same frequency
        antennas = defaultdict(list)

        for i, row in enumerate(antennas_map):
            for j, freq in enumerate(row):
                if freq not in (Cell.EMPTY, Cell.ANTINODE):
                    antennas[freq].append((i, j))

        # To track only unique positions
        antinode_positions = set()

        for same_freq in antennas.values():
            for first, second in combinations(same_freq, r=2):
                for x, y in cls.get_antinode_positions(first, second, max_x=n, max_y=m):
                    antinode_positions.add((x, y))

        return len(antinode_positions)

    @staticmethod
    def get_antinode_positions(start: Position, end: Position, max_x: int, max_y) -> Iterable[Position]:
        x1, y1 = start
        x2, y2 = end

        # Distances to antinode per axis
        dx = x1 - x2
        dy = y1 - y2

        # Left antinode position
        dx1 = x1
        dy1 = y1

        while 0 <= dx1 < max_x and 0 <= dy1 < max_y:
            yield dx1, dy1
            dx1 += dx
            dy1 += dy

        # Right antinode position
        dx2 = x2
        dy2 = y2

        while 0 <= dx2 < max_x and 0 <= dy2 < max_y:
            yield dx2, dy2
            dx2 -= dx
            dy2 -= dy


if __name__ == '__main__':
    print(Year2024Day8Part2Solution.main())
