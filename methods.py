from pathlib import Path


def get_path(day: int) -> Path:
    return Path(__file__).parent.joinpath("inputs").joinpath(f"{day}.txt")
