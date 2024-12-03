from typing import override

from infrastructure.solutions.base import Solution


class Year2019Day1Part1Solution(Solution):
    YEAR = 2019
    DAY = 1

    @override
    def parse_input(self, text_input: str) -> dict[str, list[int]]:
        masses = []

        for line in text_input.split('\n'):
            if line.isdigit():
                masses.append(int(line))

        return {'masses': masses}

    @override
    def solve(self, masses: list[int]) -> int:
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
    answer = Year2019Day1Part1Solution().main()
    print(answer)
