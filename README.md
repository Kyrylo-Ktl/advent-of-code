# Advent of Code Python Solutions

...


## Statistics

### Year 2024

|                        Task                        | Day | Part |                  Solution                  |        Time Complexity         | Space Complexity | Notes |
|:--------------------------------------------------:|:---:|:----:|:------------------------------------------:|:------------------------------:|:----------------:|-------|
| [Description](https://adventofcode.com/2024/day/1) |  1  | One  | [⭐](solutions/year_2024/day_1/part_one.py) | $O(n*\log_2{n} + m*\log_2{m})$ |     $O(n+m)$     |       |
| [Description](https://adventofcode.com/2024/day/1) |  1  | Two  | [⭐](solutions/year_2024/day_1/part_two.py) |            $O(n+m)$            |      $O(1)$      |       |
| [Description](https://adventofcode.com/2024/day/2) |  2  | One  | [⭐](solutions/year_2024/day_2/part_one.py) |            $O(n*m)$            |      $O(1)$      |       |
| [Description](https://adventofcode.com/2024/day/2) |  2  | Two  | [⭐](solutions/year_2024/day_2/part_two.py) |           $O(n*m^2)$           |      $O(m)$      |       |
| [Description](https://adventofcode.com/2024/day/3) |  3  | One  | [⭐](solutions/year_2024/day_3/part_one.py) |            $O(n*m)$            |      $O(k)$      |       |
| [Description](https://adventofcode.com/2024/day/4) |  3  | Two  | [⭐](solutions/year_2024/day_3/part_two.py) |            $O(n*m)$            |      $O(1)$      |       |
| [Description](https://adventofcode.com/2024/day/4) |  4  | One  | [-](solutions/year_2024/day_4/part_one.py) |              $-$               |       $-$        |       |
| [Description](https://adventofcode.com/2024/day/4) |  4  | Two  | [-](solutions/year_2024/day_4/part_two.py) |              $-$               |       $-$        |       |

### Year 2023

|                        Task                        | Day | Part |                  Solution                  | Time Complexity | Space Complexity | Notes |
|:--------------------------------------------------:|:---:|:----:|:------------------------------------------:|:---------------:|:----------------:|-------|
| [Description](https://adventofcode.com/2023/day/1) |  1  | One  | [⭐](solutions/year_2023/day_1/part_one.py) |    $O(n*m)$     |      $O(1)$      |       |
| [Description](https://adventofcode.com/2023/day/1) |  1  | Two  | [⭐](solutions/year_2023/day_1/part_two.py) |   $O(n*m^2)$    |      $O(m)$      |       |
| [Description](https://adventofcode.com/2023/day/2) |  2  | One  | [⭐](solutions/year_2023/day_2/part_one.py) |    $O(n*m)$     |      $O(1)$      |       |
| [Description](https://adventofcode.com/2023/day/2) |  2  | Two  | [⭐](solutions/year_2023/day_2/part_two.py) |    $O(n*m)$     |      $O(1)$      |       |


## Usage

### Setup

```dotenv
SESSION=
```

```shell
pip install -r infrastructure/requirements.txt
```

### Run 

```shell
python -m infrastructure.utils.downloader --year=2024 --day=1
```

```shell
python -m solutions.year_2024.day_2.part_two
```
