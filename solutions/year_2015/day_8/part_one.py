from typing import override

from infrastructure.solutions.base import Solution

from ast import literal_eval
class Year2015Day8Part1Solution(Solution):

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
        Time:  O(n*m)
        Space: O(1)

        Where n - numbers of strings
              m - maximum string length
        """
        characters = 0

        for string in strings:
            characters += len(string) - len(eval(string))

        return characters


if __name__ == '__main__':
    print(Year2015Day8Part1Solution.main())
