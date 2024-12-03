from sys import maxsize
from typing import override

from infrastructure.solutions.base import Solution


class Year2017Day2Part1Solution(Solution):
    YEAR = 2017
    DAY = 2

    @override
    def parse_input(self, text_input: str) -> dict[str, list[list[int]]]:
        spreadsheet = []

        for row in text_input.split('\n'):
            if not row:
                continue

            row = [int(num) for num in row.split()]
            spreadsheet.append(row)

        return {'spreadsheet': spreadsheet}

    @override
    def solve(self, spreadsheet: list[list[int]]) -> int:
        """
        Time:  O(n*m)
        Space: O(1)

        Where n - number of rows in spreadsheet
              m - maximum spreadsheet row length
        """
        checksum = 0

        for row in spreadsheet:
            minimum = maxsize
            maximum = -maxsize

            for num in row:
                minimum = min(minimum, num)
                maximum = max(maximum, num)

            checksum += maximum - minimum

        return checksum


if __name__ == '__main__':
    answer = Year2017Day2Part1Solution().main()
    print(answer)