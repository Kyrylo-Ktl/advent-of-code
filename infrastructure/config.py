import os
from datetime import date
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent.absolute()

SESSION = os.environ['SESSION']


# From the first year of the calendar to the current one
FIRST_YEAR = 2015
LAST_YEAR = date.today().year

# From the first of December to Christmas
FIRST_DAY = 1
LAST_DAY = 25

# Only two parts for each task
FIRST_PART = 1
LAST_PART = 2

# ...
INPUT_DIR = BASE_PATH / 'inputs'
INPUT_YEAR_DIR_TEMPLATE = 'Year {year}'
INPUT_DAY_DIR_TEMPLATE = 'Day {day}'
INPUT_FILE_NAME = 'input.txt'

#
SOLUTION_DIR = BASE_PATH / 'solutions'

SOLUTION_YEAR_DIR_TEMPLATE = 'year_{year}'
SOLUTION_DAY_DIR_TEMPLATE = 'day_{day}'

SOLUTION_FILE_NAME = 'part_{part}.py'


def get_input_path(year: int, day: int) -> Path:
    year = INPUT_YEAR_DIR_TEMPLATE.format(year=year)
    day = INPUT_DAY_DIR_TEMPLATE.format(day=day)

    path = INPUT_DIR / year / day

    return path


def get_input_filename(year: int, day: int) -> str:
    filename = INPUT_FILE_NAME.format(year=year, day=day)
    return filename


def get_solution_path(year: int, day: int) -> Path:
    year = SOLUTION_YEAR_DIR_TEMPLATE.format(year=year)
    day = SOLUTION_DAY_DIR_TEMPLATE.format(day=day)

    path = SOLUTION_DIR / year / day

    return path


def get_solution_filename(year: int, day: int, part: int) -> str:
    part = 'one' if part == 1 else 'two'
    filename = SOLUTION_FILE_NAME.format(year=year, day=day, part=part)
    return filename
