from methods import get_path
from rich import print as rprint

DAY = 7


class Node:
    def __init__(self, char: str, col: int, row: int):
        self.char = char
        self.col = col
        self.row = row
        self.split = False
        self.visited = False

    def print(self) -> None:
        rprint(f"{'[red]' if self.visited else '[green]'}{self.char}", end="")


class Graph:
    def __init__(self):
        self.grid: list[list[Node]] = []
        self.start: Node | None = None
        self.width = 0
        self.length = 0

        with open(get_path(DAY), "r") as f:
            for idx, line in enumerate(f):
                row: list[Node] = []
                col = 0
                for ch in line.rstrip():
                    node = Node(ch, col, idx)
                    col += 1
                    if node.char == "S":
                        self.start = node
                    row.append(node)
                    self.width = col
                self.grid.append(row)
                self.length = idx

    def print(self):
        for row in self.grid:
            for node in row:
                node.print()
            print()

    def tachyon(self, node: Node):
        if node.visited:
            return
        if node.row == self.length:
            node.visited = True
            return
        node.visited = True
        match node.char:
            case "S":
                self.tachyon(self.grid[node.row + 1][node.col])
            case ".":
                self.tachyon(self.grid[node.row + 1][node.col])
            case "^":
                node.split = True
                self.tachyon(self.grid[node.row + 1][node.col - 1])
                self.tachyon(self.grid[node.row + 1][node.col + 1])
            case _:
                raise ValueError(f"unexpected char: {node.char}")

    def count_splits(self) -> int:
        assert self.start
        self.tachyon(self.start)
        count = 0
        for row in self.grid:
            for node in row:
                if node.split:
                    count += 1
        return count


def one() -> int:
    g = Graph()
    answer = g.count_splits()
    g.print()
    return answer


def two() -> int:
    with open(get_path(DAY), "r") as f:
        pass
    return 0
