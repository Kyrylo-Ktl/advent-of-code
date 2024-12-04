from infrastructure.models import InputId

BASE_URL = 'https://adventofcode.com'

TASK_URL_TEMPLATE = BASE_URL + '/{year}/day/{day}'
INPUT_URL_TEMPLATE = TASK_URL_TEMPLATE + '/input'


def get_task_url(input_id: InputId) -> str:
    task_url = TASK_URL_TEMPLATE.format(year=input_id.year, day=input_id.day)
    return task_url


def get_input_url(input_id: InputId) -> str:
    input_url = INPUT_URL_TEMPLATE.format(year=input_id.year, day=input_id.day)
    return input_url
