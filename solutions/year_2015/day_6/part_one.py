from dataclasses import dataclass
from enum import StrEnum
from typing import override

from infrastructure.solutions.base import Solution


class Action(StrEnum):
    TURN_ON = 'turn on'
    TOGGLE = 'toggle'
    TURN_OFF = 'turn off'


@dataclass
class Cell:
    x: int
    y: int


@dataclass
class Instruction:
    action: Action
    start_cell: Cell
    end_cell: Cell


class Year2015Day6Part1Solution(Solution):
    MATRIX_WIDTH = 1_000
    MATRIX_HEIGHT = 1_000

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[Instruction]]:
        instructions = []

        for line in text_input.split('\n'):
            action, start_cell, _, end_cell = line.rsplit(maxsplit=3)

            start_x, start_y = map(int, start_cell.split(','))
            end_x, end_y = map(int, end_cell.split(','))

            instruction = Instruction(
                action=Action(action),
                start_cell=Cell(start_x, start_y),
                end_cell=Cell(end_x, end_y),
            )

            instructions.append(instruction)

        return {'instructions': instructions}

    @classmethod
    @override
    def solve(cls, instructions: list[Instruction]) -> int:
        """
        Time:  O(n*m)
        Space: O(n*m)

        Where n - number of matrix columns,
              m - number of matrix rows,
              k - number of instructions
        """
        is_turned = [[False] * cls.MATRIX_WIDTH for _ in range(cls.MATRIX_HEIGHT)]

        for instruction in instructions:
            for row in range(instruction.start_cell.x, instruction.end_cell.x + 1):
                for col in range(instruction.start_cell.y, instruction.end_cell.y + 1):
                    if instruction.action == Action.TURN_ON:
                        is_turned[row][col] = True

                    elif instruction.action == Action.TURN_OFF and is_turned[row][col] > 0:
                        is_turned[row][col] = False

                    elif instruction.action == Action.TOGGLE:
                        is_turned[row][col] = not is_turned[row][col]

        lit_count = 0

        for row in range(cls.MATRIX_HEIGHT):
            for col in range(cls.MATRIX_WIDTH):
                if is_turned[row][col]:
                    lit_count += 1

        return lit_count


if __name__ == '__main__':
    print(Year2015Day6Part1Solution.main())
