from collections import defaultdict
from sys import maxsize
from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day9Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, dict[str, dict]]:
        graph = defaultdict(dict)

        for route in text_input.split('\n'):
            connection, distance = route.split(' = ')
            start, end = connection.split(' to ')

            graph[start][end] = int(distance)
            graph[end][start] = int(distance)

        return {'graph': graph}

    @classmethod
    @override
    def solve(cls, graph: dict[str, dict]) -> int:
        """
        Time:  O(n^3)
        Space: O(n)

        Where n - number of nodes in graph
        """
        min_distance = maxsize

        for city in graph:
            distance = cls.dfs(graph, city, visited={city})
            min_distance = min(distance, min_distance)

        return min_distance

    @classmethod
    def dfs(cls, graph: dict[str, dict], curr_node: str, visited: set) -> int:
        min_distance = maxsize

        for next_node, distance in graph[curr_node].items():
            if next_node not in visited:
                visited.add(next_node)
                min_distance = min(min_distance, distance + cls.dfs(graph, next_node, visited))
                visited.remove(next_node)

        # Case when all nodes are visited
        if min_distance == maxsize:
            min_distance = 0

        return min_distance


if __name__ == '__main__':
    print(Year2015Day9Part1Solution.main())
