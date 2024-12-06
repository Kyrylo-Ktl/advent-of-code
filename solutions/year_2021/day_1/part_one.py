from itertools import pairwise
from typing import override

from infrastructure.solutions.base import Solution


class Year2021Day1Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[int]]:
        measurements = []

        for measurement in text_input.split('\n'):
            measurements.append(int(measurement))

        return {'measurements': measurements}

    @classmethod
    @override
    def solve(cls, measurements: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - number of measurements
        """
        increased_count = 0

        for prev, curr in pairwise(measurements):
            if prev < curr:
                increased_count += 1

        return increased_count


if __name__ == '__main__':
    print(Year2021Day1Part1Solution.main())
