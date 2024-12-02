from collections import Counter
from typing import override

from solutions.year_2024.day_1.part_one import Year2024Day1Part1Solution


class Year2024Day1Part2Solution(Year2024Day1Part1Solution):
    YEAR = 2024
    DAY = 1

    @override
    def solve(self, left: list[int], right: list[int]) -> int:
        """
        Time:  O(n+m)
        Space: O(1)

        Where n - size of left list,
              m - size of right list
        """
        distance = 0

        # For getting count in O(1)
        right_count = Counter(right)

        for x in left:
            distance += x * right_count[x]

        return distance


if __name__ == '__main__':
    answer = Year2024Day1Part2Solution().main()
    print(answer)
