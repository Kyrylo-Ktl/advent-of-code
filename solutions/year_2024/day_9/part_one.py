from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day9Part1Solution(Solution):

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, list[int]]:
        disk = []

        for digit in text_input:
            disk.append(int(digit))

        return {'disk': disk}

    @classmethod
    @override
    def solve(cls, disk: list[int]) -> int:
        """
        Time:  O(n*m)
        Space: O(n*m)

        Where n - disk map length,
              m - maximum block size (9 in this case)
        """
        memory = []

        for i, block_size in enumerate(disk):
            for _ in range(block_size):
                if i & 1:
                    memory.append(-1)
                else:
                    memory.append(i // 2)

        start = 0
        end = len(memory) - 1

        while start < end:
            if memory[start] != -1:
                start += 1
            elif memory[end] == -1:
                end -= 1
            else:
                memory[start] = memory[end]
                memory[end] = -1
                start += 1
                end -= 1

        checksum = 0

        for i in range(len(memory)):
            if memory[i] != -1:
                checksum += i * memory[i]

        return checksum


if __name__ == '__main__':
    print(Year2024Day9Part1Solution.main())
