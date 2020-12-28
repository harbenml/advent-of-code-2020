from collections import deque
from typing import Tuple, Deque


def get_data(fn: str) -> Tuple[Deque, Deque]:
    with open(fn) as f:
        data = f.read().split("\n\n")

    p1_raw, p2_raw = data[0], data[1]

    p1_raw = p1_raw.split(":\n")[1]
    p1_lst = [int(el) for el in p1_raw.split("\n")]
    p1 = deque(p1_lst)

    p2_raw = p2_raw.split(":\n")[1]
    p1_lst = [int(el) for el in p2_raw.split("\n")]
    p2 = deque(p1_lst)

    return p1, p2


def calc_score(p: Deque) -> int:
    return sum([(i + 1) * el for i, el in enumerate(list(p)[::-1])])


def play_next_round(p1: Deque, p2: Deque) -> Tuple[Deque, Deque]:
    c1, c2 = p1.popleft(), p2.popleft()
    if c1 > c2:
        p1.extend([c1, c2])
    else:
        p2.extend([c2, c1])
    return p1, p2


def play_game(p1: Deque, p2: Deque) -> int:
    while True:
        p1, p2 = play_next_round(p1, p2)
        if not p1 or not p2:
            print("game finished.")
            if not p2:
                return calc_score(p1)
            else:
                return calc_score(p2)


def solve_part1(fn: str):
    p1, p2 = get_data(fn)
    score = play_game(p1, p2)
    return score


if __name__ == "__main__":

    fn = "./data/data22.txt"

    score = solve_part1(fn)
    print("solution part 1:", score)

