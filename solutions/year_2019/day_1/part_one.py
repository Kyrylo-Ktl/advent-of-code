from typing import override

from infrastructure.solutions.base import Solution


class Year2019Day1Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[int]]:
        masses = []

        for line in text_input.split('\n'):
            if line.isdigit():
                masses.append(int(line))

        return {'masses': masses}

    @classmethod
    @override
    def solve(cls, masses: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - length of list with masses
        """
        fuel = 0

        for mass in masses:
            fuel += (mass // 3) - 2

        return fuel


if __name__ == '__main__':
    print(Year2019Day1Part1Solution.main())
