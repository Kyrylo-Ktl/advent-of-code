from itertools import groupby
from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day5Part1Solution(Solution):
    VOWELS = frozenset('aeiou')
    FORBIDDEN = frozenset({'ab', 'cd', 'pq', 'xy'})

    MAX_FORBIDDEN_COUNT = 0
    MIN_VOWELS_COUNT = 3
    MIN_DUPLICATES_COUNT = 1

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
        Time:  O(n*m*p*k)
        Space: O(1)

        Where n - number of strings,
              m - max string length,
              p - number of forbidden strings,
              k - max forbidden string length
        """
        nice_count = 0

        for string in strings:
            if cls.get_forbidden_count(string) > cls.MAX_FORBIDDEN_COUNT:
                continue

            if cls.get_vowels_count(string) < cls.MIN_VOWELS_COUNT:
                continue

            if cls.get_duplicates_count(string) < cls.MIN_DUPLICATES_COUNT:
                continue

            nice_count += 1

        return nice_count

    @classmethod
    def get_forbidden_count(cls, string: str) -> int:
        forbidden_count = 0

        for forbidden in cls.FORBIDDEN:
            if forbidden in string:
                forbidden_count += 1

        return forbidden_count

    @classmethod
    def get_vowels_count(cls, string: str) -> int:
        vowels_count = 0

        for char in string:
            if char in cls.VOWELS:
                vowels_count += 1

        return vowels_count

    @classmethod
    def get_duplicates_count(cls, string: str) -> int:
        duplicates_count = 0

        for char, group in groupby(string):
            if sum(1 for _ in group) >= 2:
                duplicates_count += 1

        return duplicates_count


if __name__ == '__main__':
    print(Year2015Day5Part1Solution.main())
