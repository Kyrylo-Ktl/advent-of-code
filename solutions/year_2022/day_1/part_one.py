from typing import override

from infrastructure.solutions.base import Solution


class Year2022Day1Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[int]]]:
        calories = []

        for elf_part in text_input.split('\n\n'):
            elf_cookies = []

            for cookie in elf_part.split('\n'):
                elf_cookies.append(int(cookie))

            calories.append(elf_cookies)

        return {'calories': calories}

    @classmethod
    @override
    def solve(cls, calories: list[list[int]]) -> int:
        """
        Time:  O(n*m)
        Space: O(1)

        Where n - number of elfs,
              m - max cookies per elf
        """
        max_calories = 0

        for elf_cookies in calories:
            elf_calories = sum(elf_cookies)
            max_calories = max(max_calories, elf_calories)

        return max_calories


if __name__ == '__main__':
    print(Year2022Day1Part1Solution.main())
