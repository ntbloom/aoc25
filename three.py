from methods import get_path
from collections import deque
import pytest

DAY = 3


@pytest.mark.parametrize(
    "numbers,joltage",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
        (
            "3314333333333253227333289433334173324336435282333332374344333346362333436223333531247332233332431333",
            98,
        ),
        (
            "1146336123332555645154645654113124462456216222244452524344544156456362131466166412265552465645212789",
            89,
        ),
    ],
)
def test_get_joltage(numbers: str, joltage: int):
    assert get_joltage(numbers) == joltage


@pytest.mark.parametrize(
    "numbers,joltage",
    [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ],
)
def test_get_joltage2(numbers: str, joltage: int):
    assert get_joltage2(numbers) == joltage


def get_joltage(line: str) -> int:
    nums = deque([int(ch) for ch in line.rstrip()])
    first = nums.popleft()
    second = nums.popleft()
    while len(nums) > 1:
        next = nums.popleft()
        if next > first:
            first = next
            second = nums.popleft()
            while second > first and len(nums) > 1:
                first = second
                second = nums.popleft()
            continue
        if next > second:
            second = next
    if len(nums) > 0:
        last = nums.popleft()
        if second > first:
            first = second
            second = last
        else:
            if last > second:
                second = last
    answer = (10 * first) + second
    return answer


def get_joltage2(line: str) -> int:
    def find_max(nums: list[int], length: int, answer: str) -> str:
        chunk = nums[: -(length - 1)] if length != 1 else nums
        biggest = chunk[0]
        i = 0
        for idx, val in enumerate(chunk):
            if val > biggest:
                biggest = val
                i = idx
        answer += str(biggest)
        if length == 1:
            return answer
        else:
            return find_max(nums[i + 1 :], length - 1, answer)

    nums = [int(ch) for ch in line]
    answer = find_max(nums, 12, "")
    return int(answer)


def one() -> str:
    with open(get_path(DAY), "r") as f:
        joltage = 0
        for line in f:
            joltage += get_joltage(line)
    return str(joltage)


def two() -> str:
    with open(get_path(DAY), "r") as f:
        joltage = 0
        for line in f:
            joltage += get_joltage2(line.rstrip())
    return str(joltage)
