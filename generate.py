#! /usr/bin/env -S uv run --script

from jinja2 import Environment
from pathlib import Path
import os

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

return_types = {"int": 0, "str": '""', "float": 0.0}


def create_day(day: int, return_type: str):
    filename = Path(__file__).parent.joinpath(f"{days[day]}.py")
    assert not filename.exists(), f"{filename} already exists"

    try:
        with open(filename, "w+") as f:
            env = Environment()
            with open("template.jinja", "r") as temp:
                template = env.from_string(temp.read())
            fmt = template.render({
                "day": day,
                "return_type": return_type,
                "sentinel": return_types.get(return_type, "..."),
            })
            f.write(fmt)
    except Exception as e:
        os.remove(filename)
        raise e


if __name__ == "__main__":
    from sys import argv

    match len(argv):
        case 1:
            raise ValueError("must provide day and return_type")
        case 2:
            raise ValueError("Must provide return_type")
        case 3:
            pass
        case _:
            raise ValueError("Too many command line args")
    day = int(argv[1])
    return_type = argv[2]
    create_day(day, return_type)
