from collections import Counter
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day1Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[int]]:
        left = []
        right = []

        for row in text_input.split('\n'):
            if not row:
                continue

            x, y = map(int, row.split())

            left.append(x)
            right.append(y)

        return {'left': left, 'right': right}

    @classmethod
    @override
    def solve(cls, left: list[int], right: list[int]) -> int:
        """
        Time:  O(n+m)
        Space: O(1)

        Where n - size of left list,
              m - size of right list
        """
        distance = 0

        # For getting count in O(1)
        right_count = Counter(right)

        for x in left:
            distance += x * right_count[x]

        return distance


if __name__ == '__main__':
    print(Year2024Day1Part2Solution.main())
