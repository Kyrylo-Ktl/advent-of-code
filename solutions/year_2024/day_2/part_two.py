from typing import override

from solutions.year_2024.day_2.part_one import Year2024Day2Part1Solution


class Year2024Day2Part2Solution(Year2024Day2Part1Solution):
    YEAR = 2024
    DAY = 2

    @override
    def solve(self, reports: list[list[int]]) -> int:
        """
        Time:  O(n*m^2)
        Space: O(1)

        Where n - number of records,
              m - maximum length of record
        """
        safe_count = 0

        for report in reports:
            for i in range(len(report)):
                if self.is_safe(report[:i] + report[i + 1:]):
                    safe_count += 1
                    break

        return safe_count


if __name__ == '__main__':
    Year2024Day2Part2Solution().main()
