import json
from typing import Any, override

from infrastructure.solutions.base import Solution


class Year2015Day12Part2Solution(Solution):
    FORBIDDEN_ITEMS = ('red',)

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, str]:
        return {'items': json.loads(text_input)}

    @classmethod
    @override
    def solve(cls, items: list[Any]) -> int:
        """
        Time:  O(n*m)
        Space: O(n*m)

        Where n - total number of objects,
              m - maximum size of object
        """
        items = cls.filter_forbidden(items)
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

    @classmethod
    def filter_forbidden(cls, input_obj):
        if isinstance(input_obj, dict):
            return cls.filter_forbidden_from_dict(input_obj)

        if isinstance(input_obj, list):
            return cls.filter_forbidden_from_list(input_obj)

        return input_obj

    @classmethod
    def filter_forbidden_from_dict(cls, input_dict: dict) -> dict:
        output_dict = {}

        for key, val in input_dict.items():
            if val in cls.FORBIDDEN_ITEMS:
                return {}
            output_dict[key] = cls.filter_forbidden(val)

        return output_dict

    @classmethod
    def filter_forbidden_from_list(cls, input_list: list) -> list:
        output_list = []

        for val in input_list:
            output_list.append(cls.filter_forbidden(val))

        return output_list


if __name__ == '__main__':
    print(Year2015Day12Part2Solution.main())
