from typing import List
from typing import Dict
from typing import Tuple
import re
import itertools


def update_mask(mask: str, line: str) -> str:
    return line.split(" = ")[1]


def update_mem(mem: Dict[int, int], line: str, mask: str) -> Dict[int, int]:
    # mem, mem_idx = parse_mem_line(line, mem)
    mem_idx, value = re.findall(r"\d+", line)
    mem[int(mem_idx)] = int(value)
    mem = apply_mask_to_value(mask, mem, int(mem_idx))
    return mem


def update_mem_part_2(mem: Dict[int, int], line: str, mask: str) -> Dict[int, int]:
    mem_idx, value = re.findall(r"\d+", line)
    address = apply_mask_to_address(mask, int(mem_idx))
    mem_idxs = get_mask_combinations(address)
    for idx in mem_idxs:
        mem[idx] = int(value)

    return mem


def parse_mem_line(line: str, mem: Dict[int, int]) -> Tuple[Dict[int, int], int]:
    mem_idx, value = re.findall(r"\d+", line)
    mem[int(mem_idx)] = int(value)
    return mem, int(mem_idx)


def apply_mask_to_address(mask: str, mem_idx: int) -> str:
    address = format(mem_idx, "036b")
    mask_sets = [(i, val) for i, val in enumerate(mask) if val == "X" or val == "1"]
    for i, val in mask_sets:
        address = address[:i] + val + address[i + 1 :]

    return address


def apply_mask_to_value(mask: str, mem: Dict[int, int], mem_idx: int) -> Dict[int, int]:
    value_bin = format(mem[mem_idx], "036b")
    mask_sets = [(i, val) for i, val in enumerate(mask) if val != "X"]
    for i, val in mask_sets:
        value_bin = value_bin[:i] + val + value_bin[i + 1 :]
    mem[mem_idx] = int(value_bin, 2)
    return mem


def get_mask_combinations(mask: str) -> List[int]:
    n = [i for i, val in enumerate(mask) if val == "X"]
    mem_idxs = []
    for c in itertools.product("01", repeat=len(n)):
        x = mask
        for i in range(len(n)):
            x = x[: n[i]] + c[i] + x[n[i] + 1 :]
        mem_idxs.append(int(x, 2))
    return mem_idxs


if __name__ == "__main__":

    with open("./data/data14.txt") as f:
        lines = f.read().split("\n")

    mask = "X" * 36
    mem: Dict[int, int] = {}
    mem2: Dict[int, int] = {}

    for line in lines:
        if line.split(" = ")[0] == "mask":
            mask = update_mask(mask, line)
        else:
            mem = update_mem(mem, line, mask)
            mem2 = update_mem_part_2(mem2, line, mask)

    print("Solution of part 1: ", sum(mem.values()))
    print("Solution of part 2: ", sum(mem2.values()))

