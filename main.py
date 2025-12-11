#! /usr/bin/env -S uv run --script

try:
    import one  # noqa
    import two  # noqa
    import three  # noqa
    import four  # noqa
    import five  # noqa
    import six_aoc  # noqa
    import seven  # noqa
    import eight  # noqa
    import nine  # noqa
    import ten  # noqa
    import eleven  # noqa
    import twelve  # noqa
except ImportError:
    pass


def print_puzzle(day: int, puzzle: int):
    try:
        ans = eval(f"{days[day]}.{'one' if puzzle == 1 else 'two'}()")
        print("\n-----------------------------------------------")
        print(f"Answer for day {day} puzzle {puzzle}:\n{ans}")
    except KeyError, NameError:
        raise ValueError(f"day/puzzle not done yet: day {day} puzzle {puzzle}")


if __name__ == "__main__":
    from sys import argv

    match len(argv):
        case 1:
            raise ValueError("must provide day")
        case 2:
            day = int(argv[1])
            puzzle = -1
        case 3:
            day = int(argv[1])
            puzzle = int(argv[2])
        case _:
            raise ValueError("Only day and puzzle args supported")

    assert 0 < day < 13, "must be between day 1 and 12"
    assert puzzle == 1 or puzzle == 2 or puzzle == -1, "must be puzzle 1 or 2"

    days = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six_aoc",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
    }
    if puzzle == -1:
        print_puzzle(day, 1)
        print_puzzle(day, 2)
    else:
        print_puzzle(day, puzzle)
