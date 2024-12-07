from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day8Part2Solution(Solution):

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
            characters += 2  # Quotes at the beginning and end
            characters += string.count(r'"')  # Nested quotes
            characters += string.count('\\')  # Escape chars

        return characters


if __name__ == '__main__':
    print(Year2015Day8Part2Solution.main())
