import logging

import requests

from infrastructure.models import InputId

BASE_URL = 'https://adventofcode.com'
INPUT_URL_TEMPLATE = BASE_URL + '/{year}/day/{day}/input'

logger = logging.getLogger(__name__)


class AdventOfCodeClient:

    def __init__(self, session: str):
        self.session = session

    def get_input(self, input_id: InputId) -> str:
        session = requests.Session()
        session.headers = {'cookie': f'session={self.session}'}

        input_url = INPUT_URL_TEMPLATE.format(year=input_id.year, day=input_id.day)
        logger.info(f'Downloading input from {input_url}')

        with session.get(input_url) as response:
            input_text = response.text

        return input_text
