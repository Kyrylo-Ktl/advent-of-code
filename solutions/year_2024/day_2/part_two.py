from itertools import pairwise
from typing import final, override

from infrastructure.solutions.base import Solution


class Year2024Day2Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[int]]]:
        reports = []

        for row in text_input.split('\n'):
            if not row:
                continue

            report = [int(num) for num in row.split()]
            reports.append(report)

        return {'reports': reports}

    @classmethod
    @override
    def solve(cls, reports: list[list[int]]) -> int:
        """
        Time:  O(n*m^2)
        Space: O(1)

        Where n - number of records,
              m - maximum length of record
        """
        safe_count = 0

        for report in reports:
            for i in range(len(report)):
                if cls.is_safe(report[:i] + report[i + 1:]):
                    safe_count += 1
                    break

        return safe_count

    @classmethod
    @final
    def is_safe(cls, report: list[int]) -> bool:
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
    print(Year2024Day2Part2Solution.main())
