from enum import StrEnum
from typing import override

from infrastructure.solutions.base import Solution


class Direction(StrEnum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'


class Year2021Day2Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[tuple[Direction, int]]]:
        course = []

        for line in text_input.split('\n'):
            direction, distance = line.split()

            direction = Direction(direction)
            distance = int(distance)

            course.append((direction, distance))

        return {'course': course}

    @classmethod
    @override
    def solve(cls, course: list[tuple[Direction, int]]) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - number of instructions in course
        """
        x = y = 0

        for direction, distance in course:
            match direction:
                case Direction.FORWARD:
                    x += distance
                case Direction.DOWN:
                    y += distance
                case Direction.UP:
                    y -= distance

        return x * y


if __name__ == '__main__':
    print(Year2021Day2Part1Solution.main())
