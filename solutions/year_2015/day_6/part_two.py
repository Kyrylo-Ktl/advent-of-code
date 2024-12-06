from dataclasses import dataclass
from enum import StrEnum
from typing import override

from infrastructure.solutions.base import Solution


class Action(StrEnum):
    TURN_ON = 'turn on'
    TOGGLE = 'toggle'
    TURN_OFF = 'turn off'


ACTION_INCREMENT = {
    Action.TURN_ON: 1,
    Action.TOGGLE: 2,
    Action.TURN_OFF: -1,
}


@dataclass
class Cell:
    x: int
    y: int


@dataclass
class Instruction:
    action: Action
    start: Cell
    end: Cell


class Year2015Day6Part2Solution(Solution):
    MATRIX_WIDTH = 1_000
    MATRIX_HEIGHT = 1_000

    MIN_BRIGHTNESS = 0

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
                start=Cell(start_x, start_y),
                end=Cell(end_x, end_y),
            )

            instructions.append(instruction)

        return {'instructions': instructions}

    @classmethod
    @override
    def solve(cls, instructions: list[Instruction]) -> int:
        """
        Time:  O(n*m*k)
        Space: O(n*m)

        Where n - number of matrix columns,
              m - number of matrix rows,
              k - number of instructions
        """
        brightness = [[cls.MIN_BRIGHTNESS] * cls.MATRIX_WIDTH for _ in range(cls.MATRIX_HEIGHT)]

        for instruction in instructions:
            for row in range(instruction.start.x, instruction.end.x + 1):
                for col in range(instruction.start.y, instruction.end.y + 1):
                    brightness[row][col] += ACTION_INCREMENT[instruction.action]
                    brightness[row][col] = max(brightness[row][col], cls.MIN_BRIGHTNESS)

        total_brightness = 0

        for row in range(cls.MATRIX_HEIGHT):
            for col in range(cls.MATRIX_WIDTH):
                total_brightness += brightness[row][col]

        return total_brightness


if __name__ == '__main__':
    print(Year2015Day6Part2Solution.main())
