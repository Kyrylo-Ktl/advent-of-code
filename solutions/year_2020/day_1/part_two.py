from typing import override

from infrastructure.solutions.base import Solution


class Year2020Day1Part2Solution(Solution):
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
        Time:  O(n^2)
        Space: O(1)

        Where n - expenses length
        """
        n = len(expenses)
        expenses.sort()

        for i in range(n):
            # Skipping duplicated neighbour values
            if i > 0 and expenses[i] == expenses[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                candidate_sum = expenses[i] + expenses[left] + expenses[right]

                if candidate_sum == cls.TARGET_SUM:
                    return expenses[i] * expenses[left] * expenses[right]

                if candidate_sum < cls.TARGET_SUM:
                    left += 1
                else:
                    right -= 1

        return -1


if __name__ == '__main__':
    print(Year2020Day1Part2Solution.main())
