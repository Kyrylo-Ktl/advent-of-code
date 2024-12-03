import re
from abc import ABC, abstractmethod
from typing import Any, final

from pydantic import ValidationError

from infrastructure.config import (
    get_input_filename,
    get_input_path,
    SOLUTION_CLASS_NAME_PATTERN,
    SOLUTION_CLASS_NAME_TEMPLATE,
)
from infrastructure.constants import Day, Part, Year
from infrastructure.models import SolutionId, InputId


class Solution(ABC):

    @classmethod
    @final
    def main(cls) -> Any:
        text_input = cls.read_input()

        params = cls.parse_input(text_input)

        return cls.solve(**params)

    @classmethod
    @final
    def read_input(cls) -> str:
        input_id = cls.solution_id.input_id

        file_path = get_input_path(input_id=input_id)
        file_name = get_input_filename(input_id=input_id)

        with open(file_path / file_name, 'rt') as file:
            text_input = file.read()

        return text_input

    @classmethod
    @property
    @final
    def year(cls) -> Year:
        return cls.solution_id.year

    @classmethod
    @property
    @final
    def day(cls) -> Day:
        return cls.solution_id.day

    @classmethod
    @property
    @final
    def part(cls) -> Part:
        return cls.solution_id.part

    @classmethod
    @property
    @final
    def solution_id(cls) -> SolutionId:
        match = re.match(SOLUTION_CLASS_NAME_PATTERN, cls.__name__)

        if match is None:
            raise RuntimeError(f'Solution class should be named as "{SOLUTION_CLASS_NAME_TEMPLATE}"')

        try:
            identifier = SolutionId.model_validate(match.groupdict())
        except ValidationError as exc:
            print(exc)
            raise RuntimeError(f'Solution class should be named as "{SOLUTION_CLASS_NAME_TEMPLATE}"')

        return identifier

    @classmethod
    @abstractmethod
    def parse_input(cls, text_input: str) -> dict[str, Any]:
        ...

    @classmethod
    @abstractmethod
    def solve(cls, *args, **kwargs) -> Any:
        ...
