from typing import override

from solutions.year_2017.day_1.part_one import Year2017Day1Part1Solution


class Year2017Day1Part2Solution(Year2017Day1Part1Solution):
    YEAR = 2017
    DAY = 1

    @override
    def solve(self, digits: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - number digits
        """
        n = len(digits)
        total_sum = 0

        for i in range(n):
            if digits[i] == digits[(n // 2 + i) % n]:
                total_sum += digits[i]

        return total_sum


if __name__ == '__main__':
    answer = Year2017Day1Part2Solution().main()
    print(answer)
