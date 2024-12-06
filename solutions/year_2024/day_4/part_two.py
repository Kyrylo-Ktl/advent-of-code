from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day4Part2Solution(Solution):
    STRAIGHT_TARGET = 'MAS'
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
        Time:  O(n*m*k)
        Space: O(k)

        Where n - number of rows in matrix
              m - number of columns in matrix
              k - target string length
        """
        n, m = len(matrix), len(matrix[0])
        matches = 0

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                main_diag = matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1]
                side_diag = matrix[i - 1][j + 1] + matrix[i][j] + matrix[i + 1][j - 1]

                if main_diag not in (cls.STRAIGHT_TARGET, cls.REVERSED_TARGET):
                    continue

                if side_diag not in (cls.STRAIGHT_TARGET, cls.REVERSED_TARGET):
                    continue

                matches += 1

        return matches


if __name__ == '__main__':
    print(Year2024Day4Part2Solution.main())
