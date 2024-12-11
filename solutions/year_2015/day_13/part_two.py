import re
from collections import defaultdict
from enum import StrEnum
from itertools import permutations
from typing import override

from infrastructure.solutions.base import Solution

PATTERN = r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.'


class Effect(StrEnum):
    GAIN = 'gain'
    LOSE = 'lose'


class Year2015Day13Part2Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[tuple[str, int, str]]]:
        connections = []

        for person_from, effect, score, person_to in re.findall(PATTERN, text_input):
            match effect:
                case Effect.LOSE:
                    happiness = -int(score)
                case Effect.GAIN:
                    happiness = int(score)
                case _:
                    happiness = 0

            connections.append((person_from, happiness, person_to))

        return {'connections': connections}

    @classmethod
    @override
    def solve(cls, connections: list[tuple[str, int, str]]) -> int:
        """
        Time:  O(n!)
        Space: O(n^2)

        Where ...
        """
        graph = defaultdict(dict)

        # Building directed graph from connections
        for person_from, happiness, person_to in connections:
            graph[person_from][person_to] = happiness

        # Adding myself as neutral person
        for person in list(graph.keys()):
            graph['Me'][person] = 0
            graph[person]['Me'] = 0

        max_happiness = 0
        n = len(graph)

        # Trying every possible arrangement (Hamiltonian cycle)
        for arrangement in permutations(graph):
            happiness = 0

            for i in range(n):
                # Arrangement is cycled
                person_from = arrangement[i]
                person_to = arrangement[(i + 1) % n]

                happiness += graph[person_from][person_to]
                happiness += graph[person_to][person_from]

            max_happiness = max(max_happiness, happiness)

        return max_happiness


if __name__ == '__main__':
    print(Year2015Day13Part2Solution.main())
