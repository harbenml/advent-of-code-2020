import copy
import numpy as np
from typing import Tuple


idx = acc = 0


def load_data(filename: str) -> list:
    with open(filename) as f:
        X = f.read().split("\n")
    X = [el.split(" ") for el in X]
    return X


def accumulator(value: int):
    global acc
    global idx
    acc += value
    idx += 1


def jumper(value: int):
    global idx
    idx += value


def do_nothing(value: int):
    global idx
    idx += 1


def follow_instructions(X: list) -> int:
    global acc
    global idx
    ops = {"acc": accumulator, "jmp": jumper, "nop": do_nothing}
    is_applied = [False] * len(X)
    is_success = False
    while not is_applied[idx]:
        is_applied[idx] = True
        ops[X[idx][0]](int(X[idx][1]))
        if idx >= len(X):
            is_success = True
            print("Program terminates normally.")
            break
    return acc, is_success


def permute_x_until_success(X: list) -> int:
    global acc
    global idx
    is_jmp_or_nop = [el[0] == "jmp" or el[0] == "nop" for el in X]
    idx_jmp_or_nop = list(np.where(is_jmp_or_nop)[0])
    for idx_to_swap in idx_jmp_or_nop:
        X_perm = copy.deepcopy(X)
        idx = acc = 0

        if X[idx_to_swap][0] == "jmp":
            X_perm[idx_to_swap][0] = "nop"
        if X[idx_to_swap][0] == "nop":
            X_perm[idx_to_swap][0] = "jmp"

        acc, is_success = follow_instructions(X_perm)

        if is_success:
            return acc

    return acc


if __name__ == "__main__":
    X = load_data("./data/data08.txt")
    acc, success = follow_instructions(X)
    print(acc, success)

    acc = permute_x_until_success(X)
    print(acc)
