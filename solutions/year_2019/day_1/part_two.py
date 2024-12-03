from typing import override

from solutions.year_2019.day_1.part_one import Year2019Day1Part1Solution


class Year2019Day1Part2Solution(Year2019Day1Part1Solution):
    YEAR = 2019
    DAY = 1

    @override
    def solve(self, masses: list[int]) -> int:
        """
        Time:  O(n*sqrt3(m))
        Space: O(1)

        Where n - length of list with masses
        """
        fuel = 0

        for mass in masses:
            while mass > 0:
                mass = max(0, (mass // 3) - 2)
                fuel += mass

        return fuel


if __name__ == '__main__':
    answer = Year2019Day1Part2Solution().main()
    print(answer)
