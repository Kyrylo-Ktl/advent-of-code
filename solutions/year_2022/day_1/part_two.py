from typing import override

from infrastructure.solutions.base import Solution


class Year2022Day1Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[list[int]]]:
        calories = []

        for elf_part in text_input.split('\n\n'):
            elf_cookies = []

            for cookie in elf_part.split('\n'):
                if cookie:
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
        first_max = 0
        second_max = 0
        third_max = 0

        for elf_cookies in calories:
            elf_calories = sum(elf_cookies)

            # Updating first elf calories maximum
            if elf_calories > first_max:
                third_max = second_max
                second_max = first_max
                first_max = elf_calories

            # Updating second elf calories maximum
            elif elf_calories > second_max:
                third_max = second_max
                second_max = elf_calories

            # Updating third elf calories maximum
            elif elf_calories > third_max:
                third_max = elf_calories

        return first_max + second_max + third_max


if __name__ == '__main__':
    print(Year2022Day1Part2Solution.main())
