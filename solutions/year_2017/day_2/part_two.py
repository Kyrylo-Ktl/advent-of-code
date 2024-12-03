from typing import override

from solutions.year_2017.day_2.part_one import Year2017Day2Part1Solution


class Year2017Day2Part2Solution(Year2017Day2Part1Solution):
    YEAR = 2017
    DAY = 2

    @override
    def solve(self, spreadsheet: list[list[int]]) -> int:
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
    answer = Year2017Day2Part2Solution().main()
    print(answer)
