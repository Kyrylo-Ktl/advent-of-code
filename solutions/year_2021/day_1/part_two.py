from typing import override

from infrastructure.solutions.base import Solution


class Year2021Day1Part2Solution(Solution):
    WINDOW_SIZE = 3

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
        n = len(measurements)
        increased_count = 0

        # Sliding window initialization
        curr_window_sum = 0
        for i in range(cls.WINDOW_SIZE):
            curr_window_sum += measurements[i]

        for i in range(cls.WINDOW_SIZE, n):
            next_window_sum = curr_window_sum

            # Moving sliding window forward
            next_window_sum += measurements[i]
            next_window_sum -= measurements[i - cls.WINDOW_SIZE]

            if curr_window_sum < next_window_sum:
                increased_count += 1

            curr_window_sum = next_window_sum

        return increased_count


if __name__ == '__main__':
    print(Year2021Day1Part2Solution.main())
