from methods import get_path
from collections import deque

DAY = 5


def one() -> int:
    ranges = []
    ingredients = []
    on_ranges = True
    with open(get_path(DAY), "r") as f:
        for line in f:
            if line == "\n":
                on_ranges = False
                continue
            if on_ranges:
                splits = line.rstrip().split("-")
                assert len(splits) == 2
                nums = [int(splits[0]), int(splits[1])]
                ranges.append(nums)
            else:
                ingredients.append(int(line.rstrip()))

    for r in ranges:
        assert r[0] < r[1] or r[0] == r[1]
    freshies = 0
    used = set()
    for ing in ingredients:
        for r in ranges:
            if ing >= r[0] and ing <= r[1] and ing not in used:
                used.add(ing)
                freshies += 1
    return freshies


def two() -> int:
    ranges = []
    with open(get_path(DAY), "r") as f:
        for line in f:
            if line == "\n":
                break
            splits = line.rstrip().split("-")
            assert len(splits) == 2
            first = int(splits[0])
            second = int(splits[1])
            assert second > first or first == second
            ranges.append([first, second])
    ranges.sort(key=lambda x: x[1], reverse=True)
    ranges.sort(key=lambda x: x[0], reverse=True)

    finished: list[list[int]] = []
    curr_first, curr_sec = ranges.pop()
    while len(ranges) != 0:
        first, second = ranges.pop()
        if first > curr_sec:
            finished.append([curr_first, curr_sec])
            curr_first = first
            curr_sec = second
        elif second > curr_sec:
            curr_sec = second
        elif second <= curr_sec:
            pass
        else:
            raise ValueError("unreachable")
    finished.append([curr_first, curr_sec])
    answer = 0
    for fin in finished:
        assert len(fin) == 2
        diff = 1 + fin[1] - fin[0]
        answer += diff
    return answer
