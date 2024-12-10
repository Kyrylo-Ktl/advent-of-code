from itertools import groupby
from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day10Part1Solution(Solution):
    ITERATIONS = 40

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, str]:
        return {'digits': text_input}

    @classmethod
    @override
    def solve(cls, digits: str) -> int:
        """
        Time:  O(2^n)
        Space: O(2^n)

        Where k - number of iterations to perform
        """
        curr_state = digits

        for i in range(cls.ITERATIONS):
            next_state = []

            for digit, group in groupby(curr_state):
                group_size = sum(1 for _ in group)
                next_state.append(f'{group_size}{digit}')

            curr_state = ''.join(next_state)

        return len(curr_state)


if __name__ == '__main__':
    print(Year2015Day10Part1Solution.main())
