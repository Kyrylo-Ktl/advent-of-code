from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day1Part1Solution(Solution):
    YEAR = 2024
    DAY = 1

    @override
    def parse_input(self, text_input: str) -> dict[str, list[int]]:
        left = []
        right = []

        for row in text_input.split('\n'):
            if not row:
                continue

            x, y = map(int, row.split())

            left.append(x)
            right.append(y)

        return {'left': left, 'right': right}

    @override
    def solve(self, left: list[int], right: list[int]) -> int:
        """
        Time:  O(n*log(n)+m*log(m))
        Space: O(n+m)

        Where n - size of left list,
              m - size of right list
        """
        distance = 0

        for x, y in zip(sorted(left), sorted(right)):
            distance += abs(x - y)

        return distance


if __name__ == '__main__':
    answer = Year2024Day1Part1Solution().main()
    print(answer)
