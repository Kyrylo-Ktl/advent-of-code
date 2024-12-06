from itertools import batched
from typing import override

from infrastructure.solutions.base import Solution


class Year2022Day3Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[str]]:
        rucksacks = []

        for rucksack in text_input.split('\n'):
            rucksacks.append(rucksack)

        return {'rucksacks': rucksacks}

    @classmethod
    @override
    def solve(cls, rucksacks: list[str]) -> int:
        """
        Time:  O(n*m)
        Space: O(m)

        Where n - number of rucksacks,
              m - max rucksack length
        """
        priorities = 0

        for first, second, third in batched(rucksacks, n=3):
            first_compartment = set(first)
            second_compartment = set(second)
            third_compartment = set(third)

            common_chars = first_compartment & second_compartment & third_compartment

            if not common_chars:
                continue

            # Lexicographically largest
            max_common = max(common_chars)

            if max_common.islower():
                priorities += ord(max_common) - ord('a') + 1
            else:
                priorities += ord(max_common) - ord('A') + 1 + 26

        return priorities


if __name__ == '__main__':
    print(Year2022Day3Part2Solution.main())
