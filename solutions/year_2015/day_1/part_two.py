from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day1Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, str]:
        return {'parenthesis': text_input}

    @classmethod
    @override
    def solve(cls, parenthesis: str) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - length of parenthesis
        """
        floor = 0

        for idx, bracket in enumerate(parenthesis, start=1):
            if bracket == '(':
                floor += 1
            elif bracket == ')':
                floor -= 1

            if floor < 0:
                return idx

        return -1


if __name__ == '__main__':
    print(Year2015Day1Part2Solution.main())
