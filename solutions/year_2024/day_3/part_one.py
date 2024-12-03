import re
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day3Part1Solution(Solution):
    YEAR = 2024
    DAY = 3

    @override
    def parse_input(self, text_input: str) -> dict[str, str]:
        return {'memory': text_input}

    @override
    def solve(self, memory: str) -> int:
        """
        Time:  O(n*m)
        Space: O(k)

        Where n - length of the memory string,
              m - maximum number of digits in mul expression,
              k - number of mul expressions
        """
        total_sum = 0

        for x, y in re.findall(r'mul\((\d+),(\d+)\)', memory):
            total_sum += int(x) * int(y)

        return total_sum


if __name__ == '__main__':
    answer = Year2024Day3Part1Solution().main()
    print(answer)
