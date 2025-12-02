from methods import get_path


class Dial:
    def __init__(self, start: int = 50, low: int = 0, high: int = 99):
        self._current = start
        self._low = low
        self._high = high
        self._counter = 0

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def current(self) -> int:
        return self._current

    def count(self):
        self._counter += 1

    def left(self):
        if self._current == self._low:
            self._current = self._high
        else:
            self._current -= 1

    def right(self):
        if self._current == self._high:
            self._current = self._low
        else:
            self._current += 1


def one() -> str:
    with open(get_path(1), "r") as f:
        dial = Dial(50)
        for line in f:
            direction = line[0]
            count = int(line[1:].rstrip())
            for _ in range(count):
                match direction:
                    case "L":
                        dial.left()
                    case "R":
                        dial.right()
                    case _:
                        raise ValueError("illegal direction")
            if dial.current == 0:
                dial.count()
    return str(dial.counter)


def two() -> str:
    with open(get_path(1), "r") as f:
        dial = Dial(50)
        for line in f:
            direction = line[0]
            count = int(line[1:].rstrip())
            for _ in range(count):
                match direction:
                    case "L":
                        dial.left()
                    case "R":
                        dial.right()
                    case _:
                        raise ValueError("illegal direction")
                if dial.current == 0:
                    dial.count()
    return str(dial.counter)
