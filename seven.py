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
        rprint(f"{'[red]' if self.visited else '[green]'}{self.char}", end="")

    def print_count(self) -> None:
        rprint(f"[red]C" if self.count else f"[green]{self.char}", end="")


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

    def print_count(self):
        for row in self.grid:
            for node in row:
                node.print_count()
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

    def left_parent(self, node: Node) -> Node | None:
        if node.col == 0:
            return None
        left = node.col - 1
        found = False
        idx = node.row - 1
        while not found and idx != 0:
            parent = self.grid[idx][left]
            if parent.char == "^" and parent.visited:
                return parent
            idx -= 1
        return None

    def right_parent(self, node: Node) -> Node | None:
        if node.col == self.width - 1:
            return None
        right = node.col + 1
        found = False
        idx = node.row - 1
        while not found and idx != 0:
            parent = self.grid[idx][right]
            if parent.char == "^" and parent.visited:
                return parent
            idx -= 1
        return None

    def quantum(self) -> int:
        assert self.start
        self.tachyon(self.start)

        self.start.count = 1
        for idx, row in enumerate(self.grid):
            if idx == 0:
                continue
            # mark first split manually
            elif idx == 2:
                for node in row:
                    if node.char == "^":
                        node.count = 1
                continue
            for node in row:
                left_count = 0
                right_count = 0
                if node.char == "^" and node.visited:
                    if left_up := self.left_parent(node):
                        left_count = left_up.count
                    if right_up := self.right_parent(node):
                        right_count = right_up.count
                node.count = left_count + right_count

        total = 0
        for node in self.grid[self.length]:
            count = 0
            if self.grid[self.length - 1][node.col].char == "^":
                continue
            if left := self.left_parent(node):
                count += left.count
            if right := self.right_parent(node):
                count += right.count
            node.count = count
            total += node.count
        return total

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
    g.print_count()
    return answer
