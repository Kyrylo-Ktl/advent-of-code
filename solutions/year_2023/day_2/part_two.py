from enum import StrEnum, unique
from typing import override

from solutions.year_2023.day_2.part_one import Year2023Day2Part1Solution

GAME_ID = int
CUBES_COUNT = tuple[str, int]


@unique
class CubeColor(StrEnum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


class Year2023Day2Part2Solution(Year2023Day2Part1Solution):
    YEAR = 2023
    DAY = 2

    @override
    def solve(self, games: dict[GAME_ID, list[CUBES_COUNT]]) -> int:
        total_power = 0

        for game_id, game in games.items():
            total_power += self.get_cubes_power(game)

        return total_power

    @classmethod
    def get_cubes_power(cls, game: list[CUBES_COUNT]) -> int:
        min_red = 1
        min_green = 1
        min_blue = 1

        for color, count in game:
            if color == CubeColor.RED:
                min_red = max(count, min_red)

            if color == CubeColor.GREEN:
                min_green = max(count, min_green)

            if color == CubeColor.BLUE:
                min_blue = max(count, min_blue)

        return min_red * min_green * min_blue


if __name__ == '__main__':
    answer = Year2023Day2Part2Solution().main()
    print(answer)
