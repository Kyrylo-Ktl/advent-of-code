import logging
from argparse import ArgumentParser, BooleanOptionalAction
from itertools import product

from infrastructure.commands.runner import SolutionsRunner
from infrastructure.config import get_solution_filename, get_solution_path
from infrastructure.constants import Day, Part, Year
from infrastructure.models import SolutionId
from infrastructure.solutions.base import Solution

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

parser = ArgumentParser(prog='AoC Validator')
parser.add_argument('--execute', action=BooleanOptionalAction)


class SolutionsValidator:

    def __init__(self, runner: SolutionsRunner):
        self.runner = runner

    def validate(self, execute: bool = False):
        for year, day, part in product(Year, Day, Part):
            solution_id = SolutionId(year=year, day=day, part=part)

            solution_directory = get_solution_path(solution_id=solution_id)
            solution_filename = get_solution_filename(solution_id=solution_id)
            solution_path = solution_directory / solution_filename

            if not solution_path.exists():
                continue

            logger.info(f'Found solution for {solution_id}')

            if execute:
                self.runner.run(solution_id)


if __name__ == '__main__':
    args = parser.parse_args()

    # Dependencies for validator
    runner = SolutionsRunner(Solution.__subclasses__())

    validator = SolutionsValidator(runner)
    validator.validate(execute=args.execute)
