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
        self.count = 0

    def print(self) -> None:
        rprint(
            f"{'[red]' if (self.visited or self.count) else '[green]'}{self.char}",
            end="",
        )


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

    def dump_left(self, node: Node):
        if node.col == 0:
            return
        for row in range(node.row + 1, self.length + 1):
            curr = self.grid[row][node.col - 1]
            if curr.char == "^" or row == self.length:
                curr.count += node.count
                return

    def dump_right(self, node: Node):
        if node.col == self.width:
            return
        for row in range(node.row + 1, self.length + 1):
            curr = self.grid[row][node.col + 1]
            if curr.char == "^" or row == self.length:
                curr.count += node.count
                return

    def quantum(self) -> int:
        assert self.start
        self.tachyon(self.start)

        self.start.count = 1
        for idx, row in enumerate(self.grid):
            for node in row:
                if node.char == "^":
                    if idx == 2:
                        node.count = 1
                    self.dump_left(node)
                    self.dump_right(node)
        return sum([node.count for node in self.grid[self.length]])

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
    g = Graph()
    answer = g.quantum()
    g.print()
    return answer
