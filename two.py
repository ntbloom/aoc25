from methods import get_path
import pytest

DAY = 2


def is_dupe(num: str) -> bool:
    size = len(num)
    if size % 2 != 0:
        return False
    midpoint = int(size / 2)
    first, second = num[:midpoint], num[midpoint:]
    return first == second


def is_dupe_two(num: int) -> bool:
    as_str = str(num)
    midpoint = len(as_str) // 2
    for i in range(1, midpoint + 1):
        chunk = as_str[:i]
        splits = len(as_str) // len(chunk)
        if as_str == chunk * splits:
            return True
    return False


def one() -> int:
    total = 0
    with open(get_path(DAY), "r") as f:
        nums = f.readline().rstrip().split(",")

        for group in nums:
            ranges = group.split("-")
            first = int(ranges[0])
            second = int(ranges[1])
            for entry in range(first, second + 1):
                if is_dupe(str(entry)):
                    total += entry

    return total


def two() -> int:
    total = 0
    with open(get_path(DAY), "r") as f:
        nums = f.readline().rstrip().split(",")

        for group in nums:
            ranges = group.split("-")
            first = int(ranges[0])
            second = int(ranges[1])
            for entry in range(first, second + 1):
                if is_dupe_two(entry):
                    total += entry
    return total


class TestTwo:
    @pytest.mark.parametrize(
        "num",
        (
            11,
            121212,
            7777777777,
            22,
            99,
            111,
            999,
            1010,
            1188511885,
            222222,
            446446,
            38593859,
            565565,
            824824824,
            2121212121,
        ),
    )
    def test_two(self, num: int):
        assert is_dupe_two(num)
