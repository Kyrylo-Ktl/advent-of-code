import re
from enum import StrEnum
from typing import override

from infrastructure.solutions.base import Solution


class Operation(StrEnum):
    DO = 'do()'
    DO_NOT = 'don\'t()'


class Year2024Day3Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, str]:
        return {'memory': text_input}

    @classmethod
    @override
    def solve(cls, memory: str) -> int:
        """
        Time:  O(n*m)
        Space: O(1)

        Where n - length of the memory string,
              m - maximum number of digits in mul expression
        """
        total_sum = 0
        do_mul = True

        for match in re.finditer(r'(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))', memory):
            string = match.group(0)

            if string == Operation.DO:
                do_mul = True

            elif string == Operation.DO_NOT:
                do_mul = False

            elif do_mul is True:
                x, y = re.findall(r'\d+', string)
                total_sum += int(x) * int(y)

        return total_sum


if __name__ == '__main__':
    print(Year2024Day3Part2Solution.main())
