from enum import StrEnum, unique
from typing import override

from infrastructure.solutions.base import Solution

GAME_ID = int
CUBES_COUNT = tuple[str, int]


@unique
class CubeColor(StrEnum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


class Year2023Day2Part2Solution(Solution):
    RED_CUBES = 12
    GREEN_CUBES = 13
    BLUE_CUBES = 14

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, dict[GAME_ID, list[CUBES_COUNT]]]:
        games = {}

        for line in text_input.split('\n'):
            if not line:
                continue

            # Game <ID>: <game>
            game_id, game = line.split(': ')
            game_id = int(game_id.removeprefix('Game '))

            games[game_id] = []

            # <subset1>; <subset2>; ...
            for subset in game.split('; '):
                # <cubes1>, <cubes2>, ...
                for cubes in subset.split(', '):
                    # <count> <color>
                    count, color = cubes.split()
                    games[game_id].append((color, int(count)))

        return {'games': games}

    @classmethod
    @override
    def solve(cls, games: dict[GAME_ID, list[CUBES_COUNT]]) -> int:
        """
        Time:  O(n*m)
        Space: O(1)

        Where n - total number of games,
              m - maximum game size
        """
        total_power = 0

        for game_id, game in games.items():
            total_power += cls.get_cubes_power(game)

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
    print(Year2023Day2Part2Solution.main())
