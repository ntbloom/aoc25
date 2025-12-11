from methods import get_path
from functools import reduce
import operator

DAY = 6


def one() -> int:
    lines: list[list[int]] = []
    operations: list[str] = []
    curr_line = 0
    with open(get_path(DAY), "r") as f:
        for line in f:
            curr_line += 1
            if curr_line == 5:
                for op in line.rstrip().split():
                    operations.append(op)
                continue
            nums = [int(i) for i in line.rstrip().split()]
            lines.append(nums)

    total = 0
    for i in range(1000):
        total += reduce(
            operator.mul if operations[i] == "*" else operator.add,
            [line[i] for line in lines],
        )
    return total


def ceph_math(lines: list[list[str]], operators: list[str], idx: int) -> list[int]:
    nums = []
    width = 0
    curr_width = idx + 1
    while curr_width < len(operators) and operators[curr_width] == " ":
        width += 1
        curr_width += 1
    for i in range(idx, idx + width + 1):
        num_str = ""
        for line in lines:
            ch = line[i]
            if ch != " ":
                num_str += ch
        if num_str != "":
            nums.append(int(num_str))
    return nums


def two() -> int:
    lines = []
    with open(get_path(DAY), "r") as f:
        for line in f:
            lines.append([ch for ch in line.replace("\n", "")])
    answer = 0
    operators = lines.pop()
    for idx, val in enumerate(operators):
        match val:
            case " ":
                continue
            case "*":
                op = operator.mul
            case "+":
                op = operator.add
            case _:
                raise ValueError("unexpected operator")
        answer += reduce(op, ceph_math(lines, operators, idx))
    return answer
