# Advent of Code Solutions


[![Advent of Code](https://img.shields.io/badge/Advent%20of%20Code-ffff66?logo=adventofcode&logoColor=000)](<https://adventofcode.com/> "Advent of Code homepage")
[![Made with Python](https://img.shields.io/badge/Python->=3.12-blue?logo=python&logoColor=yellow)](<https://python.org> "Python homepage")
[![Made with Docker](https://img.shields.io/badge/Docker%20Compose->=2-blue?logo=docker&logoColor=blue)](<https://docs.docker.com/compose/> "Docker Compose homepage")
![Last commit](https://img.shields.io/github/last-commit/Kyrylo-Ktl/advent-of-code "Last commit")

---

[![AoC 2024](https://img.shields.io/badge/2024-⭐%2022-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2024)
[![AoC 2023](https://img.shields.io/badge/2023-⭐%204-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2023)
[![AoC 2022](https://img.shields.io/badge/2022-⭐%202-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2022)
[![AoC 2021](https://img.shields.io/badge/2021-⭐%204-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2021)
[![AoC 2020](https://img.shields.io/badge/2020-⭐%202-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2020)
[![AoC 2019](https://img.shields.io/badge/2019-⭐%202-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2019) 
[![AoC 2018](https://img.shields.io/badge/2018-⭐%202-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2018)
[![AoC 2017](https://img.shields.io/badge/2017-⭐%202-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2017)
[![AoC 2016](https://img.shields.io/badge/2016-⭐%202-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2016)
[![AoC 2015](https://img.shields.io/badge/2015-⭐%2012-gray?logo=adventofcode&labelColor=darkgreen)](https://adventofcode.com/2015)

---

This project contains all [my](https://www.linkedin.com/in/kyrylo-ktl/) solutions for [Advent of Code](https://adventofcode.com/) challenges.

> [!WARNING]
> Note that **this project can automatically download inputs from** the Advent of Code server. Please use it moderately.

But what is Advent of Code? From the author, Eric Wastl:

> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.
>
> You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.


## Table of Contents

- [Solutions](#solutions)
  - Solutions for year [2024](#year-2024) with **11**/**25** days solved;
  - Solutions for year [2023](#year-2023) with **2**/**25** days solved;
  - Solutions for year [2022](#year-2022) with **1**/**25** days solved;
  - Solutions for year [2021](#year-2021) with **2**/**25** days solved;
  - Solutions for year [2020](#year-2020) with **1**/**25** days solved;
  - Solutions for year [2019](#year-2019) with **1**/**25** days solved;
  - Solutions for year [2018](#year-2018) with **1**/**25** days solved;
  - Solutions for year [2017](#year-2017) with **1**/**25** days solved;
  - Solutions for year [2016](#year-2016) with **1**/**25** days solved;
  - Solutions for year [2015](#year-2015) with **6**/**25** days solved;
- [Usage](#usage)
  - Project [setup](#setup) for personal usage;
  - Local [run](#local-run) of project tools;
  - Docker [run](#run-in-docker) of project tools;


## Solutions

### Year 2024

| Day | Part |                  Task description                   |                     Task input                      |                  Solution                   |        Time Complexity         | Space Complexity |      Notes       |
|:---:|:----:|:---------------------------------------------------:|:---------------------------------------------------:|:-------------------------------------------:|:------------------------------:|:----------------:|:----------------:|
|  1  | One  | [Description](https://adventofcode.com/2024/day/1)  | [Input](https://adventofcode.com/2024/day/1/input)  | [⭐](solutions/year_2024/day_1/part_one.py)  | $O(n*\log_2{n} + m*\log_2{m})$ |     $O(n+m)$     |       ...        |
|  1  | Two  | [Description](https://adventofcode.com/2024/day/1)  | [Input](https://adventofcode.com/2024/day/1/input)  | [⭐](solutions/year_2024/day_1/part_two.py)  |            $O(n+m)$            |      $O(1)$      |       ...        |
|  2  | One  | [Description](https://adventofcode.com/2024/day/2)  | [Input](https://adventofcode.com/2024/day/2/input)  | [⭐](solutions/year_2024/day_2/part_one.py)  |            $O(n*m)$            |      $O(1)$      |       ...        |
|  2  | Two  | [Description](https://adventofcode.com/2024/day/2)  | [Input](https://adventofcode.com/2024/day/2/input)  | [⭐](solutions/year_2024/day_2/part_two.py)  |           $O(n*m^2)$           |      $O(m)$      |       ...        |
|  3  | One  | [Description](https://adventofcode.com/2024/day/3)  | [Input](https://adventofcode.com/2024/day/3/input)  | [⭐](solutions/year_2024/day_3/part_one.py)  |            $O(n*m)$            |      $O(k)$      |       ...        |
|  3  | Two  | [Description](https://adventofcode.com/2024/day/3)  | [Input](https://adventofcode.com/2024/day/3/input)  | [⭐](solutions/year_2024/day_3/part_two.py)  |            $O(n*m)$            |      $O(1)$      |       ...        |
|  4  | One  | [Description](https://adventofcode.com/2024/day/4)  | [Input](https://adventofcode.com/2024/day/4/input)  | [⭐](solutions/year_2024/day_4/part_one.py)  |       $O((n+m)*(n+m)*k)$       |     $O(n*m)$     |       ...        |
|  4  | Two  | [Description](https://adventofcode.com/2024/day/4)  | [Input](https://adventofcode.com/2024/day/4/input)  | [⭐](solutions/year_2024/day_4/part_two.py)  |         $O(n * m * k)$         |      $O(k)$      |       ...        |
|  5  | One  | [Description](https://adventofcode.com/2024/day/5)  | [Input](https://adventofcode.com/2024/day/5/input)  | [⭐](solutions/year_2024/day_5/part_one.py)  |              $-$               |       $-$        | Topological sort |
|  5  | Two  | [Description](https://adventofcode.com/2024/day/5)  | [Input](https://adventofcode.com/2024/day/5/input)  | [⭐](solutions/year_2024/day_5/part_two.py)  |              $-$               |       $-$        | Topological sort |
|  6  | One  | [Description](https://adventofcode.com/2024/day/6)  | [Input](https://adventofcode.com/2024/day/6/input)  | [⭐](solutions/year_2024/day_6/part_one.py)  |            $O(n*m)$            |     $O(n*m)$     |       ...        |
|  6  | Two  | [Description](https://adventofcode.com/2024/day/6)  | [Input](https://adventofcode.com/2024/day/6/input)  | [⭐](solutions/year_2024/day_6/part_two.py)  |          $O(n^2*m^2)$          |     $O(n*m)$     |       ...        |
|  7  | One  | [Description](https://adventofcode.com/2024/day/7)  | [Input](https://adventofcode.com/2024/day/7/input)  | [⭐](solutions/year_2024/day_7/part_one.py)  |           $O(n*k^m)$           |      $O(1)$      |   Backtracking   |
|  7  | Two  | [Description](https://adventofcode.com/2024/day/7)  | [Input](https://adventofcode.com/2024/day/7/input)  | [⭐](solutions/year_2024/day_7/part_two.py)  |           $O(n*k^m)$           |      $O(m)$      |   Backtracking   |
|  8  | One  | [Description](https://adventofcode.com/2024/day/8)  | [Input](https://adventofcode.com/2024/day/8/input)  | [⭐](solutions/year_2024/day_8/part_one.py)  |          $O(n^2*m^2)$          |     $O(n*m)$     |  Linear Algebra  |
|  8  | Two  | [Description](https://adventofcode.com/2024/day/8)  | [Input](https://adventofcode.com/2024/day/8/input)  | [⭐](solutions/year_2024/day_8/part_two.py)  |   $O(n^2 * m^2 * max(n,m))$    |     $O(n*m)$     |  Linear Algebra  |
|  9  | One  | [Description](https://adventofcode.com/2024/day/9)  | [Input](https://adventofcode.com/2024/day/9/input)  | [⭐](solutions/year_2024/day_9/part_one.py)  |            $O(n*m)$            |     $O(n*m)$     |       ...        |
|  9  | Two  | [Description](https://adventofcode.com/2024/day/9)  | [Input](https://adventofcode.com/2024/day/9/input)  | [⭐](solutions/year_2024/day_9/part_two.py)  |          $O(n^2*m^2)$          |     $O(n*m)$     |       ...        |
| 10  | One  | [Description](https://adventofcode.com/2024/day/10) | [Input](https://adventofcode.com/2024/day/10/input) | [⭐](solutions/year_2024/day_10/part_one.py) |       $O(n * m * k^{2})$       |      $O(k)$      |       DFS        |
| 10  | Two  | [Description](https://adventofcode.com/2024/day/10) | [Input](https://adventofcode.com/2024/day/10/input) | [⭐](solutions/year_2024/day_10/part_two.py) |            $O(n*m)$            |     $O(n*m)$     |       DFS        |
| 11  | One  | [Description](https://adventofcode.com/2024/day/11) | [Input](https://adventofcode.com/2024/day/11/input) | [⭐](solutions/year_2024/day_11/part_one.py) |         $O(n * 2^{m})$         |  $O(n * 2^{m})$  |  DP,Memoization  |
| 11  | Two  | [Description](https://adventofcode.com/2024/day/11) | [Input](https://adventofcode.com/2024/day/11/input) | [⭐](solutions/year_2024/day_11/part_two.py) |         $O(n * 2^{m})$         |  $O(n * 2^{m})$  |  DP,Memoization  |

### Year 2023

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  | Time Complexity | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:---------------:|:----------------:|-------|
|  1  | One  | [Description](https://adventofcode.com/2023/day/1) | [Input](https://adventofcode.com/2023/day/1/input) | [⭐](solutions/year_2023/day_1/part_one.py) |    $O(n*m)$     |      $O(1)$      |       |
|  1  | Two  | [Description](https://adventofcode.com/2023/day/1) | [Input](https://adventofcode.com/2023/day/1/input) | [⭐](solutions/year_2023/day_1/part_two.py) |   $O(n*m^2)$    |      $O(m)$      |       |
|  2  | One  | [Description](https://adventofcode.com/2023/day/2) | [Input](https://adventofcode.com/2023/day/2/input) | [⭐](solutions/year_2023/day_2/part_one.py) |    $O(n*m)$     |      $O(1)$      |       |
|  2  | Two  | [Description](https://adventofcode.com/2023/day/2) | [Input](https://adventofcode.com/2023/day/2/input) | [⭐](solutions/year_2023/day_2/part_two.py) |    $O(n*m)$     |      $O(1)$      |       |

### Year 2022

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  | Time Complexity | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:---------------:|:----------------:|-------|
|  1  | One  | [Description](https://adventofcode.com/2022/day/1) | [Input](https://adventofcode.com/2022/day/1/input) | [⭐](solutions/year_2022/day_1/part_one.py) |    $O(n*m)$     |      $O(1)$      |       |
|  1  | Two  | [Description](https://adventofcode.com/2022/day/1) | [Input](https://adventofcode.com/2022/day/1/input) | [⭐](solutions/year_2022/day_1/part_two.py) |    $O(n*m)$     |      $O(1)$      |       |

### Year 2021

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  | Time Complexity | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:---------------:|:----------------:|:-----:|
|  1  | One  | [Description](https://adventofcode.com/2021/day/1) | [Input](https://adventofcode.com/2021/day/1/input) | [⭐](solutions/year_2021/day_1/part_one.py) |     $O(n)$      |      $O(1)$      |  ...  |
|  1  | Two  | [Description](https://adventofcode.com/2021/day/1) | [Input](https://adventofcode.com/2021/day/1/input) | [⭐](solutions/year_2021/day_1/part_two.py) |     $O(n)$      |      $O(1)$      |  ...  |
|  2  | One  | [Description](https://adventofcode.com/2021/day/2) | [Input](https://adventofcode.com/2021/day/2/input) | [⭐](solutions/year_2021/day_2/part_one.py) |     $O(n)$      |      $O(1)$      |  ...  |
|  2  | Two  | [Description](https://adventofcode.com/2021/day/2) | [Input](https://adventofcode.com/2021/day/2/input) | [⭐](solutions/year_2021/day_2/part_two.py) |     $O(n)$      |      $O(1)$      |  ...  |

### Year 2020

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  | Time Complexity | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:---------------:|:----------------:|-------|
|  1  | One  | [Description](https://adventofcode.com/2020/day/1) | [Input](https://adventofcode.com/2020/day/1/input) | [⭐](solutions/year_2020/day_1/part_one.py) |     $O(n)$      |      $O(n)$      |       |
|  1  | Two  | [Description](https://adventofcode.com/2020/day/1) | [Input](https://adventofcode.com/2020/day/1/input) | [⭐](solutions/year_2020/day_1/part_two.py) |    $O(n^2)$     |      $O(1)$      |       |

### Year 2019

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  |  Time Complexity  | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:-----------------:|:----------------:|-------|
|  1  | One  | [Description](https://adventofcode.com/2019/day/1) | [Input](https://adventofcode.com/2019/day/1/input) | [⭐](solutions/year_2019/day_1/part_one.py) |      $O(n)$       |      $O(1)$      |       |
|  1  | Two  | [Description](https://adventofcode.com/2019/day/1) | [Input](https://adventofcode.com/2019/day/1/input) | [⭐](solutions/year_2019/day_1/part_two.py) | $O(n*log_{3}(m))$ |      $O(1)$      |       |

### Year 2018

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  | Time Complexity | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:---------------:|:----------------:|-------|
|  1  | One  | [Description](https://adventofcode.com/2018/day/1) | [Input](https://adventofcode.com/2018/day/1/input) | [⭐](solutions/year_2018/day_1/part_one.py) |     $O(n)$      |      $O(1)$      |       |
|  1  | Two  | [Description](https://adventofcode.com/2018/day/1) | [Input](https://adventofcode.com/2018/day/1/input) | [⭐](solutions/year_2018/day_1/part_two.py) |     $O(n)$      |      $O(n)$      |       |

### Year 2017

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  |    Time Complexity     | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:----------------------:|:----------------:|-------|
|  1  | One  | [Description](https://adventofcode.com/2017/day/1) | [Input](https://adventofcode.com/2017/day/1/input) | [⭐](solutions/year_2017/day_1/part_one.py) |         $O(n)$         |      $O(1)$      |       |
|  1  | Two  | [Description](https://adventofcode.com/2017/day/1) | [Input](https://adventofcode.com/2017/day/1/input) | [⭐](solutions/year_2017/day_1/part_two.py) |         $O(n)$         |      $O(n)$      |       |
|  2  | One  | [Description](https://adventofcode.com/2017/day/2) | [Input](https://adventofcode.com/2017/day/2/input) | [⭐](solutions/year_2017/day_2/part_one.py) |        $O(n*m)$        |      $O(1)$      |       |
|  2  | Two  | [Description](https://adventofcode.com/2017/day/2) | [Input](https://adventofcode.com/2017/day/2/input) | [⭐](solutions/year_2017/day_2/part_two.py) |       $O(n*m^2)$       |      $O(1)$      |       |

### Year 2016

| Day | Part |                  Task description                  |                     Task input                     |                  Solution                  | Time Complexity | Space Complexity | Notes |
|:---:|:----:|:--------------------------------------------------:|:--------------------------------------------------:|:------------------------------------------:|:---------------:|:----------------:|-------|
|  1  | One  | [Description](https://adventofcode.com/2016/day/1) | [Input](https://adventofcode.com/2016/day/1/input) | [⭐](solutions/year_2016/day_1/part_one.py) |     $O(n)$      |      $O(1)$      |       |
|  1  | Two  | [Description](https://adventofcode.com/2016/day/1) | [Input](https://adventofcode.com/2016/day/1/input) | [⭐](solutions/year_2016/day_1/part_two.py) |    $O(n*m)$     |     $O(n*m)$     |       |

### Year 2015

| Day | Part |                  Task description                   |                     Task input                      |                  Solution                   |   Time Complexity   | Space Complexity | Notes |
|:---:|:----:|:---------------------------------------------------:|:---------------------------------------------------:|:-------------------------------------------:|:-------------------:|:----------------:|:-----:|
|  1  | One  | [Description](https://adventofcode.com/2015/day/1)  | [Input](https://adventofcode.com/2015/day/1/input)  | [⭐](solutions/year_2015/day_1/part_one.py)  |       $O(n)$        |      $O(1)$      |  ...  |
|  1  | Two  | [Description](https://adventofcode.com/2015/day/1)  | [Input](https://adventofcode.com/2015/day/1/input)  | [⭐](solutions/year_2015/day_1/part_two.py)  |       $O(n)$        |      $O(1)$      |  ...  |
|  4  | One  | [Description](https://adventofcode.com/2015/day/4)  | [Input](https://adventofcode.com/2015/day/4/input)  | [⭐](solutions/year_2015/day_4/part_one.py)  | $O((n+m) * 16^{m})$ |     $O(n+m)$     |  ...  |
|  4  | Two  | [Description](https://adventofcode.com/2015/day/4)  | [Input](https://adventofcode.com/2015/day/4/input)  | [⭐](solutions/year_2015/day_4/part_two.py)  | $O((n+m) * 16^{m})$ |     $O(n+m)$     |  ...  |
|  8  | One  | [Description](https://adventofcode.com/2015/day/8)  | [Input](https://adventofcode.com/2015/day/8/input)  | [⭐](solutions/year_2015/day_8/part_one.py)  |      $O(n*m)$       |      $O(1)$      |  ...  |
|  8  | Two  | [Description](https://adventofcode.com/2015/day/8)  | [Input](https://adventofcode.com/2015/day/8/input)  | [⭐](solutions/year_2015/day_8/part_two.py)  |      $O(n*m)$       |      $O(1)$      |  ...  |
|  9  | One  | [Description](https://adventofcode.com/2015/day/9)  | [Input](https://adventofcode.com/2015/day/9/input)  | [⭐](solutions/year_2015/day_9/part_one.py)  |      $O(n^3)$       |      $O(n)$      |  DFS  |
|  9  | Two  | [Description](https://adventofcode.com/2015/day/9)  | [Input](https://adventofcode.com/2015/day/9/input)  | [⭐](solutions/year_2015/day_9/part_two.py)  |      $O(n^3)$       |      $O(n)$      |  DFS  |
| 10  | One  | [Description](https://adventofcode.com/2015/day/10) | [Input](https://adventofcode.com/2015/day/10/input) | [⭐](solutions/year_2015/day_10/part_one.py) |      $O(2^n)$       |     $O(2^n)$     |  ...  |
| 10  | Two  | [Description](https://adventofcode.com/2015/day/10) | [Input](https://adventofcode.com/2015/day/10/input) | [⭐](solutions/year_2015/day_10/part_two.py) |      $O(2^n)$       |     $O(2^n)$     |  ...  |
| 12  | One  | [Description](https://adventofcode.com/2015/day/12) | [Input](https://adventofcode.com/2015/day/12/input) | [⭐](solutions/year_2015/day_12/part_one.py) |      $O(n*m)$       |     $O(n*m)$     |  ...  |
| 12  | Two  | [Description](https://adventofcode.com/2015/day/12) | [Input](https://adventofcode.com/2015/day/12/input) | [⭐](solutions/year_2015/day_12/part_two.py) |      $O(n*m)$       |     $O(n*m)$     |  ...  |


## Usage

### Setup

The application infrastructure code is cross-platform, so it works on Linux, macOS and Windows.
To use it, make sure you have **Python** version **3.12** or newer or **Docker** and **Docker Compose** version **2** installed
on your machine and clone the repository:

```shell
git clone https://github.com/Kyrylo-Ktl/advent-of-code
```

Move to project directory:

```shell
cd advent-of-code
```

#### Local usage

Install the required dependencies for local run:

```shell
pip install -r infrastructure/requirements.txt
```

Set necessary for downloading personalized inputs Advent of Code session cookie as environment variable:

```shell
export SESSION=<your-session-cookie>
```

> [!NOTE]
> The `SESSION` is Advent of Code session cookie. It's possible to get it by search in browser console after pressing `F12`
and going into the `Network` tab in browser. To do this it's necessary to be logged in to the site.

#### Docker usage

To run application in container, it's necessary to create and populate `.env` file before launching.
It's possible to use `.env.example` file to do this:

```dotenv
SESSION=<your-session-cookie>

YEAR=2024
DAY=1
PART=1

GID=0
UID=0
```

The `.env` file consists of several mandatory environment variables:

+ **SESSION** - Advent of Code session cookie;


+ **YEAR** - task year for running commands;
+ **DAY** - task day for running commands;
+ **PART** - task part for running commands;


+ **UID** - in Linux a UID (User Identifier) is a unique number assigned to each user on a system.
  It identifies the user for system processes, permissions, and ownership of files or directories.
  The **root** user by default has an UID equal to **0**, in case the application is run under a different user account
  it's possible to check current UID using the following command:
  ```shell
  id --user ${whoami}
  ```
  More about [UID](https://www.cbtnuggets.com/blog/technology/system-admin/linux-file-permission-uid-vs-gid).


+ **GID** - In Linux, a GID (Group Identifier) is a unique number assigned to each group on the system. 
  It is used to define the ownership of files, directories, and processes at the group level.
  The **root** user by default has an GID equal to **0**, in case the application is run under a different user account
  it's possible to check current GID using the following command:
  ```shell
  id --group ${whoami}
  ```
  More about [GID](https://www.cbtnuggets.com/blog/technology/system-admin/linux-file-permission-uid-vs-gid).


### Local Run

To download personalized task input use:

```shell
python -m infrastructure.commands.downloader --year=2024 --day=1
```

To run task solution use:

```shell
python -m infrastructure.commands.runner --year=2024 --day=1 --part=1
```

To validate all tasks solutions:

```shell
python -m infrastructure.commands.validator --execute
```

### Run in Docker

To download personalized task input use:

```shell
docker compose up advent-of-code-downloader --build
```

To run task solution use:

```shell
docker compose up advent-of-code-runner --build
```

To validate all tasks solutions:

```shell
docker compose up advent-of-code-validator --build
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## License

This project is licensed under the MIT License - see the [license](LICENSE) file for details.


## Happy adventure! ⭐
