from collections import defaultdict
from sys import maxsize
from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day9Part2Solution(Solution):

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
        max_distance = -maxsize

        for city in graph:
            distance = cls.dfs(graph, city, visited={city})
            max_distance = max(distance, max_distance)

        return max_distance

    @classmethod
    def dfs(cls, graph: dict[str, dict], curr_node: str, visited: set) -> int:
        max_distance = -maxsize

        for next_node, distance in graph[curr_node].items():
            if next_node not in visited:
                visited.add(next_node)
                max_distance = max(max_distance, distance + cls.dfs(graph, next_node, visited))
                visited.remove(next_node)

        # Case when all nodes are visited
        if max_distance == -maxsize:
            max_distance = 0

        return max_distance


if __name__ == '__main__':
    print(Year2015Day9Part2Solution.main())
