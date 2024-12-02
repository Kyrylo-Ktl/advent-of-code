from typing import override

from infrastructure.solutions.base import Solution


class Year2023Day1Part1Solution(Solution):
    YEAR = 2023
    DAY = 1

    @override
    def parse_input(self, text_input: str) -> dict[str, list[str]]:
        lines = []

        for line in text_input.split('\n'):
            if not line:
                continue
            lines.append(line)

        return {'lines': lines}

    @override
    def solve(self, lines: list[str]) -> int:
        """
        Time:  O(n*m)
        Space: O(1)

        Where n - number of lines,
              m - max line length
        """
        total_calibration = 0

        for line in lines:
            total_calibration += self.get_calibration(line)

        return total_calibration

    @classmethod
    def get_calibration(cls, line: str) -> int:
        m = len(line)
        left, right = 0, m - 1

        while left <= m - 1 and not line[left].isdigit():
            left += 1

        while right >= 0 and not line[right].isdigit():
            right -= 1

        if line[left].isdigit() and line[right].isdigit():
            return int(line[left] + line[right])

        return 0


if __name__ == '__main__':
    answer = Year2023Day1Part1Solution().main()
    print(answer)
