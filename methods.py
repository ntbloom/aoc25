from pathlib import Path


def get_path(day: int) -> Path:
    input_file = Path(__file__).parent.joinpath("inputs").joinpath(f"{day}.txt")
    assert input_file.exists(), f"Missing input for day {day}"
    return input_file
