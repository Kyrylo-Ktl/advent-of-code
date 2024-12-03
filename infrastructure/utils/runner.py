import logging
from argparse import ArgumentParser
from typing import Type

from infrastructure.constants import Day, Part, Year
from infrastructure.models import SolutionId
from infrastructure.solutions.base import Solution
from solutions import *  # noqa

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

parser = ArgumentParser(prog='AoC Runner')
parser.add_argument('--year', required=True, type=int, choices=list(Year))
parser.add_argument('--day', required=True, type=int, choices=list(Day))
parser.add_argument('--part', required=True, type=int, choices=list(Part))


class SolutionsRunner:

    def __init__(self, solutions: list[Type[Solution]]):
        self.solutions = self._prepare_solutions(solutions)

    @staticmethod
    def _prepare_solutions(solutions: list[Type[Solution]]) -> dict[SolutionId, Type[Solution]]:
        solutions_map = {}

        for solution_cls in solutions:
            solution_id = solution_cls.solution_id

            if solution_id in solutions_map:
                raise ValueError(f'Duplicate solution {solution_cls} and {solutions_map[solution_id]}')

            solutions_map[solution_id] = solution_cls

        return solutions_map

    def run(self, year: int, day: int, part: int):
        solution_id = SolutionId(year=year, day=day, part=part)

        if solution_id not in self.solutions:
            raise ValueError('Not solved yet')

        solution = self.solutions[solution_id]

        logger.info(f'Answer for year {year}, day {day}, part {part} task:  {solution.main()}')


if __name__ == '__main__':
    args = parser.parse_args()

    runner = SolutionsRunner(Solution.__subclasses__())
    runner.run(year=args.year, day=args.day, part=args.part)
