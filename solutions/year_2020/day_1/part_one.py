from typing import override

from infrastructure.solutions.base import Solution


class Year2020Day1Part1Solution(Solution):
    TARGET_SUM = 2020

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[int]]:
        expenses = []

        for record in text_input.split('\n'):
            expenses.append(int(record))

        return {'expenses': expenses}

    @classmethod
    @override
    def solve(cls, expenses: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(n)

        Where n - expenses length
        """
        seen_records = set()

        for record in expenses:
            if cls.TARGET_SUM - record in seen_records:
                return record * (cls.TARGET_SUM - record)
            seen_records.add(record)

        return -1


if __name__ == '__main__':
    print(Year2020Day1Part1Solution.main())
