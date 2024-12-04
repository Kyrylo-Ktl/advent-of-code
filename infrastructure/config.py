import os
from pathlib import Path

from infrastructure.models import InputId, SolutionId

BASE_PATH = Path(__file__).parent.parent.absolute()

# ...
INPUT_DIR = BASE_PATH / 'inputs'
INPUT_YEAR_DIR_TEMPLATE = 'Year {year}'
INPUT_DAY_DIR_TEMPLATE = 'Day {day}'
INPUT_FILE_NAME = 'input.txt'

#
SOLUTION_DIR_NAME = 'solutions'
SOLUTION_DIR = BASE_PATH / SOLUTION_DIR_NAME

SOLUTION_YEAR_DIR_TEMPLATE = 'year_{year}'
SOLUTION_DAY_DIR_TEMPLATE = 'day_{day}'

SOLUTION_FILE_NAME = 'part_{part}.py'

# ...
SOLUTION_CLASS_NAME_TEMPLATE = 'Year{year}Day{day}Part{part}Solution'
SOLUTION_CLASS_NAME_PATTERN = r'Year(?P<year>\d{4})Day(?P<day>\d{1,2})Part(?P<part>\d)Solution'


def get_session() -> str:
    session = os.environ.get('SESSION')

    if not session:
        raise RuntimeError('SESSION environment variable is undefined.')

    return session


def get_input_path(input_id: InputId) -> Path:
    year = INPUT_YEAR_DIR_TEMPLATE.format(year=input_id.year)
    day = INPUT_DAY_DIR_TEMPLATE.format(day=input_id.day)

    path = INPUT_DIR / year / day

    return path


def get_input_filename(input_id: InputId) -> str:
    filename = INPUT_FILE_NAME.format(year=input_id.year, day=input_id.day)
    return filename


def get_solution_path(solution_id: SolutionId) -> Path:
    year = SOLUTION_YEAR_DIR_TEMPLATE.format(year=solution_id.year)
    day = SOLUTION_DAY_DIR_TEMPLATE.format(day=solution_id.day)

    path = SOLUTION_DIR / year / day

    return path


def get_solution_module(solution_id: SolutionId) -> str:
    year = SOLUTION_YEAR_DIR_TEMPLATE.format(year=solution_id.year)
    day = SOLUTION_DAY_DIR_TEMPLATE.format(day=solution_id.day)
    file = get_input_filename(solution_id)

    module = f'{SOLUTION_DIR_NAME}.{year}.{day}.{file}'

    return module


def get_solution_filename(solution_id: SolutionId) -> str:
    part = 'one' if solution_id.part == 1 else 'two'
    filename = SOLUTION_FILE_NAME.format(year=solution_id.year, day=solution_id.day, part=part)
    return filename
