from typing import override

from infrastructure.solutions.base import Solution


class Year2017Day1Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[int]]:
        digits = []

        for char in text_input:
            if char.isdigit():
                digits.append(int(char))

        return {'digits': digits}

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
    print(Year2017Day1Part2Solution.main())
