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
            if not p2:
                return calc_score(p1)
            else:
                return calc_score(p2)


def play_recursive_game(p1: Deque, p2: Deque) -> Tuple[int, int]:
    prev = set()
    while True:
        state = (tuple(p1), tuple(p2))
        if state in prev:
            # player 1 wins
            return 1, calc_score(p1)
        else:
            prev.add(state)
            c1, c2 = p1.popleft(), p2.popleft()
            if len(p1) >= c1 and len(p2) >= c2:
                if not p1:
                    return 2, calc_score(p1)
                elif not p2:
                    return 1, calc_score(p1)
                else:
                    p1sub, p2sub = list(p1)[:c1], list(p2)[:c2]
                    winner, _ = play_recursive_game(deque(p1sub), deque(p2sub))
            else:
                winner = 1 if c1 > c2 else 2

        if winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

        if not p1:
            return 2, calc_score(p2)
        elif not p2:
            return 1, calc_score(p1)


def solve_part1(fn: str):
    p1, p2 = get_data(fn)
    score = play_game(p1, p2)
    return score


def solve_part2(fn: str):
    p1, p2 = get_data(fn)
    _, score = play_recursive_game(p1, p2)
    return score


if __name__ == "__main__":

    fn = "./data/data22.txt"

    score = solve_part1(fn)
    print("solution part 1:", score)

    score2 = solve_part2(fn)
    print("solution part 2:", score2)
