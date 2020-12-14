from puzzles.puzzle14 import update_mask
from puzzles.puzzle14 import update_mem
from puzzles.puzzle14 import update_mem_part_2

from typing import Dict


def test_part_1():

    with open("./data/test_data14.txt") as f:
        lines = f.read().split("\n")

    mask = "X" * 36
    mem: Dict[int, int] = {}
    for line in lines:
        if line.split(" = ")[0] == "mask":
            mask = update_mask(mask, line)
        else:
            mem = update_mem(mem, line, mask)
    assert sum(mem.values()) == 165


def test_part_2():

    with open("./data/test_data14_2.txt") as f:
        lines = f.read().split("\n")

    mask = "X" * 36
    mem2: Dict[int, int] = {}

    for line in lines:
        if line.split(" = ")[0] == "mask":
            mask = update_mask(mask, line)
        else:
            mem2 = update_mem_part_2(mem2, line, mask)

    assert sum(mem2.values()) == 208
