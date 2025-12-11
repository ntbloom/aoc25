from methods import get_path

from math import sqrt
from itertools import combinations
from functools import reduce
from operator import mul

DAY = 8


class JunctionBox:
    def __init__(self, line: str):
        splits = line.split(",")
        assert len(splits) == 3
        self.x = int(splits[0])
        self.y = int(splits[1])
        self.z = int(splits[2])
        self.neighbors: set[JunctionBox] = set()
        self.visited = False

    def distance(self, other: JunctionBox) -> float:
        return sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def __repr__(self) -> str:
        return f"x={self.x},y={self.y},z={self.z}"


class Graph:
    def __init__(self, input: list[str], length: int):
        res: list[JunctionBox] = []
        for line in input:
            res.append(JunctionBox(line))
        results = list(combinations(res, 2))
        results.sort(key=lambda x: x[0].distance(x[1]), reverse=True)
        self.sorted_distances = results
        self.boxes: set[JunctionBox] = set()
        self.length = length
        self.node_counter = 0
        self.marked: tuple[JunctionBox, JunctionBox] | None = None
        self.single: set[JunctionBox] = set()
        self.remaining: set[JunctionBox] = set()

        for _ in range(self.length):
            first, second = self.sorted_distances.pop()
            self.boxes.add(first)
            self.boxes.add(second)
            self.remaining.add(first)
            self.remaining.add(second)
            first.neighbors.add(second)
            second.neighbors.add(first)

    def count(self, box: JunctionBox):
        if box.visited:
            return
        box.visited = True
        self.boxes.remove(box)
        self.node_counter += 1
        for neighbor in box.neighbors:
            self.count(neighbor)

    def solve(self) -> int:
        lengths: list[int] = []
        while len(self.boxes) != 0:
            curr = self.boxes.pop()
            self.boxes.add(curr)
            self.count(curr)
            lengths.append(self.node_counter)
            self.node_counter = 0
        lengths.sort(reverse=True)
        return reduce(mul, lengths[:3])


def one() -> int:
    lines: list[str] = []
    with open(get_path(DAY), "r") as f:
        for line in f:
            lines.append(line.rstrip())
    g = Graph(lines, 1000)
    return g.solve()


class Graph2:
    def __init__(self, input: list[str]):
        res: list[JunctionBox] = []
        for line in input:
            res.append(JunctionBox(line))
        results = list(combinations(res, 2))
        results.sort(key=lambda x: x[0].distance(x[1]), reverse=True)
        self.sorted_distances: list[tuple[JunctionBox, JunctionBox]] = results
        for val in self.sorted_distances:
            print(val)
        self.boxes: set[JunctionBox] = set()
        self.marked: tuple[JunctionBox, JunctionBox] | None = None
        self.single: set[JunctionBox] = set()

    def solve(self) -> int:
        main_set: set[JunctionBox] = set()
        aux_sets: list[set[JunctionBox]] = []
        first, second = self.sorted_distances.pop()
        main_set.add(first)
        main_set.add(second)

        current = self.sorted_distances.pop()
        main_set.add(current[0])
        main_set.add(current[1])
        iters = 0

        print()
        while len(aux_sets) != 0 or iters < 5:
            iters += 1
            current = self.sorted_distances.pop()
            print()
            print(f"{main_set=}(len={len(main_set)})")
            print(f"{aux_sets=}(len={len(aux_sets)})")
            print(f"{current=}")
            one, two = current

            # see if any sets are populated
            found_sets = []
            for s in aux_sets:
                if one in s or two in s:
                    print("found in aux")
                    found_sets.append(s)
                    s.add(one)
                    s.add(two)

            # reduce aux sets
            match len(found_sets):
                case 0:
                    print("no matches in aux")
                    if one in main_set or two in main_set:
                        print("found match in main")
                        main_set.add(one)
                        main_set.add(two)
                    else:
                        aux_sets.append(set([one, two]))
                        print("making new set")
                    continue
                case _:
                    first_set = found_sets.pop()
                    for remaining in found_sets:
                        print("combining with another set")
                        first_set |= remaining
                        aux_sets.remove(remaining)

                    if one in main_set or two in main_set:
                        print("combining with main set")
                        main_set |= first_set
                        aux_sets.remove(first_set)

        print(f"{iters=},{len(self.sorted_distances)=}")
        print(f"{current=}")
        return current[0].x * current[1].x


def two() -> int:
    lines: list[str] = []
    with open(get_path(DAY), "r") as f:
        for line in f:
            lines.append(line.rstrip())
    g = Graph2(lines)
    return g.solve()


if __name__ == "__main__":
    inputs = [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]
    g = Graph2(inputs)
    print(g.solve())
