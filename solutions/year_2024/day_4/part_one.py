from collections import defaultdict
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day4Part1Solution(Solution):
    STRAIGHT_TARGET = 'XMAS'
    REVERSED_TARGET = STRAIGHT_TARGET[::-1]

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[str]]:
        matrix = []

        for line in text_input.split('\n'):
            if line:
                matrix.append(line)

        return {'matrix': matrix}

    @classmethod
    @override
    def solve(cls, matrix: list[str]) -> int:
        """
        Time:  O((n+m)*(n+m)*k)
        Space: O(n*m)

        Where n - number of rows in matrix
              m - number of columns in matrix
              k - target string length
        """
        matches = 0

        for row in cls.get_rows(matrix):
            matches += row.count(cls.STRAIGHT_TARGET)
            matches += row.count(cls.REVERSED_TARGET)

        for column in cls.get_columns(matrix):
            matches += column.count(cls.STRAIGHT_TARGET)
            matches += column.count(cls.REVERSED_TARGET)

        for diagonal in cls.get_main_diagonals(matrix):
            matches += diagonal.count(cls.STRAIGHT_TARGET)
            matches += diagonal.count(cls.REVERSED_TARGET)

        for diagonal in cls.get_side_diagonals(matrix):
            matches += diagonal.count(cls.STRAIGHT_TARGET)
            matches += diagonal.count(cls.REVERSED_TARGET)

        return matches

    @classmethod
    def get_rows(cls, matrix: list[str]) -> list[str]:
        return [row for row in matrix]

    @classmethod
    def get_columns(cls, matrix: list[str]) -> list[str]:
        return [''.join(column) for column in zip(*matrix)]

    @classmethod
    def get_main_diagonals(cls, matrix: list[str]) -> list[str]:
        diagonals = defaultdict(list)

        for i, row in enumerate(matrix):
            for j, char in enumerate(row):
                diagonals[i - j].append(char)

        return [''.join(diagonal) for diagonal in diagonals.values()]

    @classmethod
    def get_side_diagonals(cls, matrix: list[str]) -> list[str]:
        diagonals = defaultdict(list)

        for i, row in enumerate(matrix):
            for j, char in enumerate(row):
                diagonals[i + j].append(char)

        return [''.join(diagonal) for diagonal in diagonals.values()]


if __name__ == '__main__':
    print(Year2024Day4Part1Solution.main())
