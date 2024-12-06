from collections import defaultdict
from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day5Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, dict | list]:
        rules = defaultdict(set)
        updates = []

        page_ordering, page_updates = text_input.split('\n\n')

        for rule in page_ordering.split('\n'):
            first, second = map(int, rule.split('|'))
            rules[first].add(second)

        for update in page_updates.split('\n'):
            updates.append(list(map(int, update.split(','))))

        return {'rules': rules, 'updates': updates}

    @classmethod
    @override
    def solve(cls, rules: dict[int, set], updates: list[list[int]]) -> int:
        valid_sum = 0

        for update in updates:
            is_valid = True
            seen = set()

            for page in update:
                if rules[page] & seen:
                    is_valid = False
                seen.add(page)

            if is_valid:
                valid_sum += update[len(update) // 2]

        return valid_sum


if __name__ == '__main__':
    print(Year2024Day5Part1Solution.main())
