import logging
import os
from argparse import ArgumentParser

from infrastructure.aoc.client import AdventOfCodeClient
from infrastructure.config import get_input_filename, get_input_path, get_session
from infrastructure.constants import Day, Year
from infrastructure.models import InputId

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

parser = ArgumentParser(prog='AoC Downloader')
parser.add_argument('--year', required=True, type=int, choices=list(Year))
parser.add_argument('--day', required=True, type=int, choices=list(Day))


class InputsDownloader:

    def __init__(self, client: AdventOfCodeClient):
        self.client = client

    def download(self, year: int, day: int):
        input_id = InputId(year=year, day=day)

        input_text = self.client.get_input(input_id=input_id)
        input_path = get_input_path(input_id=input_id)
        input_name = get_input_filename(input_id=input_id)

        # For creating nested folders structure
        os.makedirs(input_path, exist_ok=True)

        with open(input_path / input_name, 'wt') as file:
            file.write(input_text)

        logger.info(f'Saved year {year}, day {day} task input to {input_path / input_name}')


if __name__ == '__main__':
    args = parser.parse_args()

    # Dependencies for downloader
    session = get_session()
    client = AdventOfCodeClient(session=session)

    downloader = InputsDownloader(client=client)
    downloader.download(year=args.year, day=args.day)
