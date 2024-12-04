import logging

import requests

from infrastructure.aoc.config import get_input_url
from infrastructure.models import InputId

logger = logging.getLogger(__name__)


class AdventOfCodeClient:

    def __init__(self, session: str):
        self.session = session

    def get_input(self, input_id: InputId) -> str:
        session = requests.Session()
        session.headers = {'cookie': f'session={self.session}'}

        input_url = get_input_url(input_id=input_id)
        logger.info(f'Downloading input from {input_url}')

        with session.get(input_url) as response:
            input_text = response.text

        return input_text
