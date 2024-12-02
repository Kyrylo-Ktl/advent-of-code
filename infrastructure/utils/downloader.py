import logging
import os
from argparse import ArgumentParser

from infrastructure.aoc.client import AdventOfCodeClient
from infrastructure.config import (
    FIRST_DAY,
    FIRST_YEAR,
    get_input_filename,
    get_input_path,
    LAST_DAY,
    LAST_YEAR,
    SESSION,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

parser = ArgumentParser(prog='AoC Downloader')
parser.add_argument('--year', required=True, type=int, choices=range(FIRST_YEAR, LAST_YEAR + 1))
parser.add_argument('--day', required=True, type=int, choices=range(FIRST_DAY, LAST_DAY + 1))


def prepare_input(year: int, day: int):
    client = AdventOfCodeClient(session=SESSION)

    input_path = get_input_path(year=year, day=day)
    input_name = get_input_filename(year=year, day=day)
    input_text = client.get_input(year=year, day=day)

    # For creating nested folders structure
    os.makedirs(input_path, exist_ok=True)

    with open(input_path / input_name, 'wt') as file:
        file.write(input_text)

    logger.info(f'Saved year {year}, day {day} task input to {input_path / input_name}')


if __name__ == '__main__':
    args = parser.parse_args()
    prepare_input(year=args.year, day=args.day)
