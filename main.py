import one


def main():
    print("Hello from aoc25!")


if __name__ == "__main__":
    from sys import argv

    day = int(argv[1])
    puzzle = int(argv[2])
    assert 0 < day < 13, "must be between day 1 and 12"
    assert puzzle == 1 or puzzle == 2, "must be puzzle 1 or 2"

    days = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
    }
    try:
        print(eval(f"{days[day]}.{'one' if puzzle == 1 else 'two'}()"))
    except Exception:
        raise ValueError(f"day/puzzle not done yet: day {day} puzzle {puzzle}")
