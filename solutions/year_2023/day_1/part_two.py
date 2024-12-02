from typing import override

from solutions.year_2023.day_1.part_one import Year2023Day1Part1Solution

WORD_TO_NUMBER_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


class Year2023Day1Part2Solution(Year2023Day1Part1Solution):

    @override
    def solve(self, lines: list[str]) -> int:
        """
        Time:  O(n*m^2)
        Space: O(m)

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

        while left <= m - 1 and not line[left].isdigit() and cls.get_prefix_number(line, left) is None:
            left += 1

        while right >= 0 and not line[right].isdigit() and cls.get_suffix_number(line, right) is None:
            right -= 1

        first_digit = cls.get_prefix_number(line, left)
        second_digit = cls.get_suffix_number(line, right)

        if first_digit is None and line[left].isdigit():
            first_digit = line[left]

        if second_digit is None and line[right].isdigit():
            second_digit = line[right]

        if first_digit is not None and second_digit is not None:
            return int(first_digit + second_digit)

        return 0

    @staticmethod
    def get_prefix_number(line: str, start: int) -> str:
        for word, number in WORD_TO_NUMBER_MAP.items():
            if line.startswith(word, start):
                return number

    @staticmethod
    def get_suffix_number(line: str, end: int) -> str:
        for word, number in WORD_TO_NUMBER_MAP.items():
            if line.endswith(word, 0, end + 1):
                return number


if __name__ == '__main__':
    answer = Year2023Day1Part2Solution().main()
    print(answer)
