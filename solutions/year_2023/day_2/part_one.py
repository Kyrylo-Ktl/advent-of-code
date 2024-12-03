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


class Year2023Day2Part1Solution(Solution):
    YEAR = 2023
    DAY = 2

    RED_CUBES = 12
    GREEN_CUBES = 13
    BLUE_CUBES = 14

    @override
    def parse_input(self, text_input: str) -> dict[str, dict[GAME_ID, list[CUBES_COUNT]]]:
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

    @override
    def solve(self, games: dict[GAME_ID, list[CUBES_COUNT]]) -> int:
        """
        Time:  O(n*m)
        Space: O(1)

        Where n - total number of games,
              m - maximum game size
        """
        ids_sum = 0

        for game_id, game in games.items():
            if self.is_game_possible(game):
                ids_sum += game_id

        return ids_sum

    @classmethod
    def is_game_possible(cls, game: list[CUBES_COUNT]) -> bool:
        for color, count in game:
            if color == CubeColor.RED and count > cls.RED_CUBES:
                return False

            if color == CubeColor.GREEN and count > cls.GREEN_CUBES:
                return False

            if color == CubeColor.BLUE and count > cls.BLUE_CUBES:
                return False

        return True


if __name__ == '__main__':
    answer = Year2023Day2Part1Solution().main()
    print(answer)
