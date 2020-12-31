"""

        (-1,1) nw    ne (1,1)

     (-2,0) w    (0,0)   e (2,0)

       (-1,-1) sw   se (1,-1)

"""
from typing import Callable, Iterable, List, NamedTuple, Generator


def parse(line: str) -> List:
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


data = get_data("./data/test_data24.txt")
data = [parse(line) for line in data]

print(data)


# t = (0, 0)
# d = ["nw", "w", "sw", "e", "e"]
# for move in map(move_fun, ["e", "se", "w"]):
#     t = move(*t)
