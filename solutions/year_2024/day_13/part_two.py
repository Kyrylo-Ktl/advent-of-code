import re
from dataclasses import dataclass
from typing import override

from infrastructure.solutions.base import Solution

PATTERN = (
    r'Button A: X\+(\d+), Y\+(\d+)\n'
    r'Button B: X\+(\d+), Y\+(\d+)\n'
    r'Prize: X=(\d+), Y=(\d+)'
)


@dataclass
class Game:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    prize_x: int
    prize_y: int


class Year2024Day13Part2Solution(Solution):
    A_TOKENS = 3
    B_TOKENS = 1

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[Game]]:
        games = []

        for a_x, a_y, b_x, b_y, prize_x, prize_y in re.findall(PATTERN, text_input):
            game = Game(
                a_x=int(a_x),
                a_y=int(a_y),

                b_x=int(b_x),
                b_y=int(b_y),

                prize_x=int(prize_x) + 10_000_000_000_000,
                prize_y=int(prize_y) + 10_000_000_000_000,
            )

            games.append(game)

        return {'games': games}

    @classmethod
    @override
    def solve(cls, games: list[Game]) -> int:
        """
        Time:  O(n)
        Space: O(1)

        Where n - number of games
        """
        tokens = 0

        for game in games:
            a_times, b_times = cls.min_tokens(game)

            # Number of presses must be non-negative
            if a_times < 0 or b_times < 0:
                continue

            # Number of presses must be non-integer
            if not a_times.is_integer() or not b_times.is_integer():
                continue

            tokens += int(a_times) * cls.A_TOKENS + int(b_times) * cls.B_TOKENS

        return tokens

    @classmethod
    def min_tokens(cls, game: Game) -> tuple[float, float]:
        a_times = (game.prize_x * game.b_y - game.prize_y * game.b_x) / (game.a_x * game.b_y - game.a_y * game.b_x)
        b_times = (game.prize_x * game.a_y - game.prize_y * game.a_x) / (game.b_x * game.a_y - game.b_y * game.a_x)
        return a_times, b_times


if __name__ == '__main__':
    print(Year2024Day13Part2Solution.main())
