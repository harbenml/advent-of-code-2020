from itertools import product
from collections import defaultdict


def get_data(filename: str, dimension: int):
    with open(filename) as f:
        cube = f.read().splitlines()
    if dimension == 3:
        active = [
            (x, y, 0)
            for x, row in enumerate(cube)
            for y, el in enumerate(row)
            if el == "#"
        ]
    elif dimension == 4:
        active = [
            (x, y, 0, 0)
            for x, row in enumerate(cube)
            for y, el in enumerate(row)
            if el == "#"
        ]
    return active


def simulate_one_cycle(active: list, dimension: int) -> list:
    neighbors = defaultdict(lambda: 0)
    active_new = []
    for cube in active:
        for diff in product([-1, 0, 1], repeat=dimension):
            neighbor = tuple(i + j for i, j in zip(cube, diff))
            if neighbor != cube:
                neighbors[neighbor] += 1
    for cube, value in neighbors.items():
        if cube in active and 2 <= value <= 3:
            active_new.append(cube)
        elif cube not in active and value == 3:
            active_new.append(cube)
    return active_new


if __name__ == "__main__":

    filename = "./data/data17.txt"
    for dimension in [3, 4]:
        active = get_data(filename, dimension)
        for _ in range(6):
            active = simulate_one_cycle(active, dimension)
        print(len(active))

