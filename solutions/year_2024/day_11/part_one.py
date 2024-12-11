from functools import cache
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day11Part1Solution(Solution):
    BLINKS = 25

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[str]]:
        return {'stones': text_input.split()}

    @classmethod
    @override
    def solve(cls, stones: list[str]) -> int:
        """
        Time:  O(n*2^m)
        Space: O(n*2^m)

        Where n - number of stones
              m - number of blinks
        """
        length = 0

        for stone in stones:
            length += cls.get_stones_count(stone=stone, blinks=cls.BLINKS)

        return length

    @classmethod
    @cache
    def get_stones_count(cls, stone: str, blinks: int) -> int:
        # No blinks, one stone
        if blinks == 0:
            return 1

        # Case for splitting into two stones
        if not len(stone) & 1:
            middle = len(stone) // 2

            left_stone = str(int(stone[:middle]))
            right_stone = str(int(stone[middle:]))

            return cls.get_stones_count(left_stone, blinks - 1) + cls.get_stones_count(right_stone, blinks - 1)

        # Case with zero substitution
        if stone == '0':
            return cls.get_stones_count('1', blinks - 1)

        # Default case with multiplication by 2024
        return cls.get_stones_count(str(int(stone) * 2024), blinks - 1)


if __name__ == '__main__':
    print(Year2024Day11Part1Solution.main())
