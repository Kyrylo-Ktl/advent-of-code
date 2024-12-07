from itertools import product
from typing import override

from infrastructure.solutions.base import Solution

Equation = tuple[int, list[int]]

OPERATIONS = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '||': lambda x, y: int(str(x) + str(y)),
}


class Year2024Day7Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[Equation]]:
        equations = []

        for line in text_input.split('\n'):
            answer, expression = line.split(': ')

            answer = int(answer)
            expression = [int(num) for num in expression.split()]

            equations.append((answer, expression))

        return {'equations': equations}

    @classmethod
    @override
    def solve(cls, equations: list[Equation]) -> int:
        """
        Time:  O(n*k^m)
        Space: O(m)

        Where n - number of equations,
              m - maximum size of equation
              k - number of possible operations
        """
        possible_sum = 0

        for answer, expression in equations:
            for operations in product(OPERATIONS.keys(), repeat=len(expression) - 1):
                possible_answer = expression[0]

                for i, operation in enumerate(operations, start=1):
                    possible_answer = OPERATIONS[operation](possible_answer, expression[i])

                    # Early break for exceeded value
                    if possible_answer > answer:
                        break

                if possible_answer == answer:
                    possible_sum += answer
                    break

        return possible_sum


if __name__ == '__main__':
    print(Year2024Day7Part2Solution.main())
