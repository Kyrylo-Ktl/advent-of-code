from typing import override

from infrastructure.solutions.base import Solution


class Year2024Day9Part2Solution(Solution):

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
        Time:  O(n^2*m^2)
        Space: O(n^2*m^2)

        Where n - disk map length,
              m - maximum block size (9 in this case)
        """
        file_blocks = []
        free_blocks = []

        memory_idx = 0

        for i, block_size in enumerate(disk):
            if i & 1:
                free_blocks.append((block_size, memory_idx))
            else:
                file_blocks.append((block_size, memory_idx, i // 2))

            memory_idx += block_size

        memory = []

        for file_block_size, file_block_start, file_id in reversed(file_blocks):
            block_start = file_block_start
            block_end = block_start + file_block_size - 1

            for i, (free_block_size, memory_idx) in enumerate(free_blocks):
                # Free block slot is exhausted
                if free_block_size == 0:
                    continue

                # Free block placed after current one
                if file_block_start < memory_idx:
                    break

                # Cutting necessary part from free block
                if free_block_size >= file_block_size:
                    free_blocks[i] = (free_block_size - file_block_size, memory_idx + file_block_size)
                    block_start = memory_idx
                    block_end = memory_idx + file_block_size - 1
                    break

            memory.append((file_id, block_start, block_end))

        checksum = 0

        for file_id, start_idx, end_idx in memory:
            checksum += file_id * cls.get_range_sum(start_idx - 1, end_idx)

        return checksum

    @staticmethod
    def get_range_sum(n: int, m: int) -> int:
        return (m * (m + 1) - n * (n + 1)) // 2


if __name__ == '__main__':
    print(Year2024Day9Part2Solution.main())
