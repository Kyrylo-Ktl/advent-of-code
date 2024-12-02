from abc import ABC, abstractmethod
from typing import Any, final

from infrastructure.config import get_input_filename, get_input_path


class Solution(ABC):
    YEAR: int
    DAY: int

    @final
    def main(self) -> Any:
        text_input = self.read_input()

        params = self.parse_input(text_input)

        return self.solve(**params)

    @final
    def read_input(self) -> str:
        file_path = get_input_path(year=self.YEAR, day=self.DAY)
        file_name = get_input_filename(year=self.YEAR, day=self.DAY)

        with open(file_path / file_name, 'rt') as file:
            text_input = file.read()

        return text_input

    @abstractmethod
    def parse_input(self, text_input: str) -> dict[str, Any]:
        ...

    @abstractmethod
    def solve(self, *args, **kwargs) -> Any:
        ...
