from hashlib import md5
from typing import override

from infrastructure.solutions.base import Solution


class Year2015Day4Part1Solution(Solution):
    HASH_PREFIX = '00000'

    @classmethod
    @override
    def parse_input(cls, text_input: str) -> dict[str, str]:
        return {'secret_key': text_input}

    @classmethod
    @override
    def solve(cls, secret_key: str) -> int:
        """
        Time:  O((n+m)*16^m)
        Space: O(n+m)

        Where n - length of secret key
              m - length of pattern (5 in this case)
        """
        min_number = 0

        while not cls.get_hash(secret_key, min_number).startswith(cls.HASH_PREFIX):
            min_number += 1

        return min_number

    @staticmethod
    def get_hash(secret_key: str, min_number: int) -> str:
        return md5((secret_key + str(min_number)).encode()).hexdigest()


if __name__ == '__main__':
    print(Year2015Day4Part1Solution.main())
