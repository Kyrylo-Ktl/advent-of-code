import re
from dataclasses import dataclass
from typing import override

from infrastructure.solutions.base import Solution

PATTERN = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'


@dataclass
class Robot:
    p_x: int
    p_y: int
    v_x: int
    v_y: int


class Year2024Day14Part1Solution(Solution):
    WIDTH = 101
    HEIGHT = 103

    SECONDS = 100

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[Robot]]:
        robots = []

        for p_x, p_y, v_x, v_y in re.findall(PATTERN, text_input):
            robot = Robot(
                p_x=int(p_x),
                p_y=int(p_y),

                v_x=int(v_x),
                v_y=int(v_y),
            )

            robots.append(robot)

        return {'robots': robots}

    @classmethod
    @override
    def solve(cls, robots: list[Robot]) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - number of robots
        """
        x_middle = cls.WIDTH // 2
        y_middle = cls.HEIGHT // 2

        first_quad = 0
        second_quad = 0
        third_quad = 0
        fourth_quad = 0

        for robot in robots:
            x = (robot.p_x + cls.SECONDS * robot.v_x) % cls.WIDTH
            y = (robot.p_y + cls.SECONDS * robot.v_y) % cls.HEIGHT

            # Bottom left quadrant
            if x < x_middle and y < y_middle:
                first_quad += 1

            # Top left quadrant
            elif x > x_middle and y < y_middle:
                second_quad += 1

            # Bottom right quadrant
            elif x < x_middle and y > y_middle:
                third_quad += 1

            # Top right quadrant
            elif x > x_middle and y > y_middle:
                fourth_quad += 1

        return first_quad * second_quad * third_quad * fourth_quad


if __name__ == '__main__':
    print(Year2024Day14Part1Solution.main())
