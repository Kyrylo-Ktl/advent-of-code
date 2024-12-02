from itertools import pairwise
from typing import final, override

from infrastructure.solution import Solution


class Year2024Day2Part1Solution(Solution):
    YEAR = 2024
    DAY = 2

    @override
    def parse_input(self, text_input: str) -> dict[str, list[list[int]]]:
        reports = []

        for row in text_input.split('\n'):
            if not row:
                continue

            report = [int(num) for num in row.split()]
            reports.append(report)

        return {'reports': reports}

    @override
    def solve(self, reports: list[list[int]]) -> int:
        """
        Time:  O(n*m)
        Space: O(1)

        Where n - number of records,
              m - maximum length of record
        """
        safe_count = 0

        for report in reports:
            if self.is_safe(report):
                safe_count += 1

        return safe_count

    @final
    def is_safe(self, report: list[int]) -> bool:
        is_decreasing = True
        is_increasing = True

        for x, y in pairwise(report):
            # Checking if safe
            if not (1 <= abs(x - y) <= 3):
                return False

            if x > y:
                is_increasing = False

            if x < y:
                is_decreasing = False

        return is_decreasing or is_increasing


if __name__ == '__main__':
    answer = Year2024Day2Part1Solution().main()
    print(answer)
