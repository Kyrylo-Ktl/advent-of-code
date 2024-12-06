from typing import override

from infrastructure.solutions.base import Solution


class Year2018Day1Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[int]]:
        frequency_changes = []

        for changes in text_input.split('\n'):
            for change in changes.split(', '):
                frequency_changes.append(int(change))

        return {'frequency_changes': frequency_changes}

    @classmethod
    @override
    def solve(cls, frequency_changes: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - number of frequency changes
        """
        frequency = 0

        for change in frequency_changes:
            frequency += change

        return frequency


if __name__ == '__main__':
    print(Year2018Day1Part1Solution.main())
