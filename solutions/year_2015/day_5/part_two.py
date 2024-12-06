from itertools import product
from string import ascii_lowercase
from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day5Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[str]]:
        strings = []

        for line in text_input.split('\n'):
            strings.append(line)

        return {'strings': strings}

    @classmethod
    @override
    def solve(cls, strings: list[str]) -> int:
        """
        Time:  O(n*m*k^2)
        Space: O(1)

        Where n - number of strings,
              m - max string length,
              k - alphabet size (26 in this case)
        """
        nice_count = 0

        for string in strings:
            if cls.contains_pair(string) and cls.contains_triplet(string):
                nice_count += 1

        return nice_count

    @classmethod
    def contains_pair(cls, string: str) -> bool:
        for a, b in product(ascii_lowercase, ascii_lowercase):
            if string.count(a + b) >= 2:
                return True
        return False

    @classmethod
    def contains_triplet(cls, string: str) -> bool:
        for a, b in product(ascii_lowercase, ascii_lowercase):
            if a + b + a in string:
                return True
        return False


if __name__ == '__main__':
    print(Year2015Day5Part2Solution.main())
