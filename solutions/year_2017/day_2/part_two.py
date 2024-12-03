from typing import override

from infrastructure.solutions.base import Solution


class Year2017Day2Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[int]]]:
        spreadsheet = []

        for row in text_input.split('\n'):
            if not row:
                continue

            row = [int(num) for num in row.split()]
            spreadsheet.append(row)

        return {'spreadsheet': spreadsheet}

    @classmethod
    @override
    def solve(cls, spreadsheet: list[list[int]]) -> int:
        """
        Time:  O(n*m^2)
        Space: O(1)

        Where n - number of rows in spreadsheet
              m - maximum spreadsheet row length
        """
        checksum = 0

        for row in spreadsheet:
            for x in row:
                for y in row:
                    if x != y and not x % y:
                        checksum += x // y

        return checksum


if __name__ == '__main__':
    print(Year2017Day2Part2Solution.main())
