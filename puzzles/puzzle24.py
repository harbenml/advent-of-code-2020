"""

        (-1,1) nw    ne (1,1)

     (-2,0) w    (0,0)   e (2,0)

       (-1,-1) sw   se (1,-1)

"""
from typing import (
    Callable,
    Iterable,
    List,
    NamedTuple,
    Generator,
    Optional,
    Set,
    Tuple,
    cast,
)
from collections import Counter


def parse(line: str) -> List[str]:
    instructions = []
    while line:
        if line[:2] in ("se", "sw", "nw", "ne"):
            instructions.append(line[:2])
            line = line[2:]
        else:
            instructions.append(line[0])
            line = line[1:]
    return instructions


def get_data(fn: str) -> List[str]:
    with open(fn) as f:
        data = f.read().split("\n")
    return data


def move_fun(direction: str) -> Callable:
    if direction == "e":
        return lambda x, y: (x + 2, y)
    elif direction == "se":
        return lambda x, y: (x + 1, y - 1)
    elif direction == "sw":
        return lambda x, y: (x - 1, y - 1)
    elif direction == "w":
        return lambda x, y: (x - 2, y)
    elif direction == "nw":
        return lambda x, y: (x - 1, y + 1)
    elif direction == "ne":
        return lambda x, y: (x + 1, y + 1)

    return lambda x, y: (x, y)


def find_tile(instructions: List[str], t: Tuple[int, int] = (0, 0)) -> Tuple[int, int]:
    for move in map(move_fun, instructions):
        t = move(*t)
    return t


def solve_part1(data: List[str]) -> Set[Tuple[int, int]]:
    black_tiles = set()
    for line in data:
        instructions = parse(line)
        tile = find_tile(instructions)
        if tile not in black_tiles:
            black_tiles.add(tile)
        else:
            black_tiles.remove(tile)
    return black_tiles


def get_neighbors(
    tile: Tuple[int, int], black_tiles: Set[Tuple[int, int]], neighbor_counts: Counter
) -> Counter:

    for move in map(move_fun, ["e", "se", "sw", "w", "nw", "ne"]):
        neighbor = move(*tile)
        neighbor_counts[neighbor] += 1
    return neighbor_counts


def flip_one_cycle(black_tiles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    neighbor_counts: Counter = Counter()
    for tile in black_tiles:
        neighbor_counts = get_neighbors(tile, black_tiles, neighbor_counts)

    new_black_tiles: Set[Tuple[int, int]] = set()
    for neighbor, count in neighbor_counts.items():
        if (neighbor in black_tiles and 1 <= count <= 2) or (
            neighbor not in black_tiles and count == 2
        ):
            new_black_tiles.add(neighbor)
    return new_black_tiles


def solve_part2(black_tiles: Set[Tuple[int, int]]) -> int:
    for _ in range(100):
        black_tiles = flip_one_cycle(black_tiles)
    return len(black_tiles)


if __name__ == "__main__":

    data = get_data("./data/test_data24.txt")

    black_tiles = solve_part1(data)
    print(len(black_tiles))

    num_black_tiles = solve_part2(black_tiles)
    print(num_black_tiles)

