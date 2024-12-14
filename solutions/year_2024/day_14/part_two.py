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


class Year2024Day14Part2Solution(Solution):
    WIDTH = 101
    HEIGHT = 103

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
        Time:  O(∞)
        Space: O(n)

        Where n - number of robots
        """
        seconds = 0

        # Indicates that there is no overlap between robot positions
        is_valid = False

        while not is_valid:
            seconds += 1

            positions = set()
            is_valid = True

            for robot in robots:
                x = (robot.p_x + seconds * robot.v_x) % cls.WIDTH
                y = (robot.p_y + seconds * robot.v_y) % cls.HEIGHT

                # Two robots in the same position
                if (x, y) in positions:
                    is_valid = False
                    break

                positions.add((x, y))

        return seconds


if __name__ == '__main__':
    print(Year2024Day14Part2Solution.main())
