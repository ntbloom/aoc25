from methods import get_path
from rich import print
from collections import deque

DAY = 4

WIDTH = 139
LENGTH = 139


class Node:
    def __init__(self, row: int, col: int, char: str):
        self._row = row
        self._col = col
        self._char = char
        assert self._char == "@" or self._char == "."
        self._north: Node | None = None
        self._northwest: Node | None = None
        self._west: Node | None = None
        self._southwest: Node | None = None
        self._south: Node | None = None
        self._southeast: Node | None = None
        self._east: Node | None = None
        self._northeast: Node | None = None

        self._picked = False

    def __repr__(self) -> str:
        return self._char

    def find_neighbors(self, grid: list[list[Node]]):
        # north
        if self._row != 0:
            self._north = grid[self._row - 1][self._col]
        # northwest
        if self._row != 0 and self._col != 0:
            self._northwest = grid[self._row - 1][self._col - 1]
        # west
        if self._col != 0:
            self._west = grid[self._row][self._col - 1]
        # southwest
        if self._col != 0 and self._row != LENGTH - 1:
            self._southwest = grid[self._row + 1][self._col - 1]
        # south
        if self._row != LENGTH - 1:
            self._south = grid[self._row + 1][self._col]
        # southeast
        if self._row != LENGTH - 1 and self._col != WIDTH - 1:
            self._southeast = grid[self._row + 1][self._col + 1]
        # east
        if self._col != WIDTH - 1:
            self._east = grid[self._row][self._col + 1]
        # northeast
        if self._row != 0 and self._col != WIDTH - 1:
            self._northeast = grid[self._row - 1][self._col + 1]

    def accessible(self) -> bool:
        if self._char == "@":
            count = 0
            for neighbor in (
                self._north,
                self._northwest,
                self._west,
                self._southwest,
                self._south,
                self._southeast,
                self._east,
                self._northeast,
            ):
                if neighbor and neighbor._char == "@":
                    count += 1
            return count < 4
        return False

    def remove(self):
        assert self._char == "@"
        self._char = "."


def build_grid() -> list[list[Node]]:
    with open(get_path(DAY), "r") as f:
        row_idx = 0
        col_idx = 0

        cols: list[list[Node]] = []
        for line in f:
            row: list[Node] = []
            for ch in line.strip():
                row.append(Node(row_idx, col_idx, ch))
                col_idx += 1

            assert len(row) == WIDTH
            cols.append(row)
            row_idx += 1
            col_idx = 0
    assert len(cols) == LENGTH
    for row in cols:
        for node in row:
            node.find_neighbors(cols)
    return cols


def one() -> int:
    count = 0
    for row in build_grid():
        for node in row:
            if node.accessible():
                count += 1
            #     print(f"[blue]{node._char}", end="")
            # else:
            #     print(f"[red]{node._char}", end="")
        # print(end="")

    return count


def two() -> int:
    count = 0
    queue: deque[Node] = deque()
    grid = build_grid()
    for row in grid:
        for node in row:
            if node.accessible() and not node._picked:
                queue.append(node)
                node._picked = True
    while len(queue) != 0:
        node = queue.pop()
        count += 1
        node.remove()

        for neighbor in [
            node._north,
            node._northwest,
            node._west,
            node._southwest,
            node._south,
            node._southeast,
            node._east,
            node._northeast,
        ]:
            if neighbor:
                neighbor.find_neighbors(grid)
                if neighbor.accessible() and not neighbor._picked:
                    queue.append(neighbor)
                    neighbor._picked = True
    return count
