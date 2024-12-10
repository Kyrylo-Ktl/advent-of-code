import json
from typing import Any, override

from infrastructure.solutions.base import Solution


class Year2015Day12Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, str]:
        return {'items': json.loads(text_input)}

    @classmethod
    @override
    def solve(cls, items: list[Any]) -> int:
        """
        Time:  O(n*m)
        Space: O(m)

        Where n - total number of objects,
              m - maximum size of object
        """
        return cls.sum_numbers(items)

    @classmethod
    def sum_numbers(cls, item: Any) -> int:
        if isinstance(item, dict):
            return sum(cls.sum_numbers(value) for value in item.values())

        if isinstance(item, list):
            return sum(cls.sum_numbers(value) for value in item)

        if isinstance(item, int):
            return item

        return 0


if __name__ == '__main__':
    print(Year2015Day12Part1Solution.main())
